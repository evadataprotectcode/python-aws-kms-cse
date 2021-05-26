'use strict';

const Fs = require('fs');
const ProgressBar = require('progress');
const {PassThrough} = require('stream');
const {once} = require('events');

const Cse = require('./aws/cse');
const S3 = require('./aws/s3');

const internals = {};


exports.download = async function(filePath, bucketName, s3Key, cseKeyArn) {
  const {ContentLength} = await S3.headObject(bucketName, s3Key);

  const progress = new ProgressBar('  downloading [:bar] :percent :etas', {
    complete: '=',
    incomplete: ' ',
    width: 20,
    total: ContentLength
  });


  const writeStream = Fs.createWriteStream(filePath)

  const passThrough = new PassThrough();
  const s3Stream = internals.getObjectStream(bucketName, s3Key, cseKeyArn, passThrough);
  const fileStream = s3Stream.pipe(writeStream);

  passThrough.on('data', function (chunk) {
    progress.tick(chunk.length);
  });

  await once(fileStream, 'finish');
};

internals.getObjectStream = function(bucketName, s3Key, cseKeyArn, passThrough) {
  const s3Stream = S3.getObjectStream(bucketName, s3Key).pipe(passThrough);

  if(cseKeyArn) {
   return s3Stream.pipe(Cse.decryptStream(cseKeyArn));
  }

  return s3Stream;
};
