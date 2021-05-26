'use strict';

const Path = require('path');
const Bossy = require('@hapi/bossy');
const App = require('./lib');

const internals = {};

internals.definition = {
  h: {
    description: 'Show help',
    alias: 'help',
    type: 'boolean'
  },
  u: {
    description: 'Upload a file',
    alias: 'upload',
    type: 'boolean',
  },
  d: {
    description: 'Download a file',
    alias: 'download',
    type: 'boolean',
  },
  f: {
    description: 'File to upload/download',
    alias: 'file',
    type: 'string',
    require: true
  },
  b: {
    description: 'S3 bucket name to upload/download',
    alias: 's3Bucket',
    type: 'string',
    require: true
  },
  k: {
    description: 'KMS key arn to use to encrypt the file',
    alias: 'kmsArn',
    type: 'string',
  }
};

internals.run = async function () {
  const args = Bossy.parse(internals.definition);

  if (args instanceof Error) {
    return console.error(args.message);
  }

  if(args.upload && args.download) {
    return console.log('Please choose either upload or download, not both');
  }

  const {file, s3Bucket, kmsArn} = args;

  if(args.upload) {
    return internals.upload(file, s3Bucket, kmsArn);
  }

  if(args.download) {
    return internals.download(file, s3Bucket, kmsArn);
  }

  console.log('You must specify either --upload or --download')
  return console.log(Bossy.usage(internals.definition));
};

internals.upload = async function(file, s3Bucket, kmsArn) {
  const s3Key = Path.basename(file);

  return await App.upload(file, s3Bucket, s3Key, kmsArn);
};

internals.download = async function(file, s3Bucket, kmsArn) {
  const filePath = Path.join(__dirname, file);

  console.log(`File will be available here ${filePath}`);

  return await App.download(filePath, s3Bucket, file, kmsArn);
}

internals.run().catch(console.error).finally(process.exit);