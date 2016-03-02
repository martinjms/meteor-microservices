Meteor.methods({
  processImage: (image) => {
    imageProcessor.call('process',image, (error, result) => (error)?console.log(error):console.log(result));
    console.log('processImage');
  }
})
