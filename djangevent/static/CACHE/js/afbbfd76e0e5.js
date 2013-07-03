"use strict";

var eventsApp = angular.module('EventsApp', []);

eventsApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

"use strict";

eventsApp.controller("EventController", function EventController($scope, $http) {
    $scope.events = [];

    $scope.init = function () {
        $http({method: "GET", url: "/events"}).
        success(function (data, status, header, config) {
            $scope.events = data;
        })
        .error(function (data, status, header, config) {
            console.log(data, status, header, config);
        });
    }
});
