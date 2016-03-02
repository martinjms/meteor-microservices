angular.module('biotools',['angular-meteor', 'ui.router']);

angular.module('biotools').config(function($urlRouterProvider, $stateProvider, $locationProvider){

  $locationProvider.html5Mode(true);

  $stateProvider.state('home', {
      url: '/home',
      template: '<home></home>'
    });
  $urlRouterProvider.otherwise("/home");
});
