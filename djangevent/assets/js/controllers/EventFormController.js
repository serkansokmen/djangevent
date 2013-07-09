'use strict';

eventsApp.controller('EventFormController', function EventFormController($scope, $http) {
    $scope.event = [];

    $scope.saveEvent = function (event, newEventForm) {
        if (newEventForm.$valid) {
            console.log('valid');
        } else {
            console.log('not valid');
        }
    };
 });
