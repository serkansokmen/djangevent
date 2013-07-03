"use strict";

eventsApp.controller("EventsController", function EventsController($scope, $http) {
    $scope.events = [];
    $scope.currentEvent = null;

    $scope.sortOrder = 'name';

    $scope.init = function () {
        $http({method: "GET", url: "/events/api/"}).
        success(function (data, status, header, config) {
            $scope.events = data;
            if (data.length > 0) {
                $scope.currentEvent = data[0];
            }
        })
        .error(function (data, status, header, config) {
            console.log(data, status, header, config);
        });
    };

    $scope.setCurrentEvent = function(event) {
        $scope.currentEvent = event;
    }

    $scope.upVoteSession = function (session) {
        session.voteCount++;
    };
    $scope.downVoteSession = function (session) {
        session.voteCount--;
    };
});
