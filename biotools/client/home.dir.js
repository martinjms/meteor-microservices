angular.module('biotools')

.directive('home', function(){
  return {
    templateUrl: 'client/home.tmpl.html',
    controller: function ($scope, $meteor) {
        $scope.image='an image';
        $scope.click = () => {
          console.log('click');
          Meteor.call('processImage',$scope.image)
        };
    }
  }
});
