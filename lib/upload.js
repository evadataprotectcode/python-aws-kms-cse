'use strict';

const Fs = require('fs');
const ProgressBar = require('progress');
const {PassThrough} = require('stream');

const Cse = require('./aws/cse');
const S3 = require('./aws/s3');

const internals = {};


exports.upload = async function (filePath, bucketName, s3Key, cseKeyArn) {
  const passThrough = new PassThrough();
  const fileStream = internals.getUploadStream(filePath, cseKeyArn, passThrough);
  const fileStats = Fs.statSync(filePath);

  const progress = new ProgressBar('  uploading [:bar] :percent :etas', {
    complete: '=',
    incomplete: ' ',
    width: 20,
    total: fileStats.size
  });

  passThrough.on('data', function (chunk) {
    progress.tick(chunk.length);
  });

  return await S3.upload(fileStream, bucketName, s3Key);
};

internals.getUploadStream = function(filePath, cseKeyArn, passThrough) {
  const fileStream = Fs.createReadStream(filePath).pipe(passThrough);

  if(cseKeyArn) {
   return fileStream.pipe(Cse.encryptStream(cseKeyArn));
  }

  return fileStream;
};
