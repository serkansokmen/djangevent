"use strict";

eventsApp.controller("EventController", function EventController($scope, $http) {
    $scope.events = [];
    $scope.currentEvent = null;

    $scope.init = function () {
        $http({method: "GET", url: "/events"}).
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
