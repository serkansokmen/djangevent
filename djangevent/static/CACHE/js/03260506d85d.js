"use strict";

var eventsApp = angular.module('EventsApp', []);

eventsApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

"use strict";

eventsApp.controller("EventController", function EventController($scope) {
    $scope.message = "Hello Events";
});
