'use strict';

const AWS = require('aws-sdk');

const S3 = new AWS.S3();


exports.getObjectStream = function(bucketName, key) {
  const params = {
    Bucket: bucketName,
    Key: key
  };

  return S3.getObject(params).createReadStream();
};

exports.headObject = async function(bucketName, key) {
  const params = {
    Bucket: bucketName,
    Key: key
  };

  return await S3.headObject(params).promise();
};


exports.upload = async function(readableStream, bucketName, key) {
  const params = {
    Bucket: bucketName,
    Key: key,
    Body: readableStream
  };

  return S3.upload(params).promise();
};
