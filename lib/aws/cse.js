'use strict';

const {KmsKeyringNode, buildClient, CommitmentPolicy} = require('@aws-crypto/client-node');


const {encryptStream, decryptStream} = buildClient(CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT);


exports.encryptStream = function(keyArn) {
  const keyring = new KmsKeyringNode({generatorKeyId: keyArn});
  return encryptStream(keyring);
};

exports.decryptStream = function(keyArn) {
  const keyring = new KmsKeyringNode({generatorKeyId: keyArn});
  return decryptStream(keyring);
};
