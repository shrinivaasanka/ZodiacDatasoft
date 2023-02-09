/**
 * @license
 * Copyright 2019 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */

//import dotenv from "dotenv";

function initMap(): void {
  /*
  var latitude = 13.067439;
  var longitude = 80.237617;
  */
  var latitudeenv = parseFloat(import.meta.env.VITE_LATITUDE);
  var longitudeenv = parseFloat(import.meta.env.VITE_LONGITUDE);
  console.log(import.meta.env);
  const map = new google.maps.Map(
    document.getElementById("map") as HTMLElement,
    {
      zoom: 13,
      center: { lat: latitudeenv, lng: longitudeenv },
    }
  );

  const trafficLayer = new google.maps.TrafficLayer();

  trafficLayer.setMap(map);
}

declare global {
  interface Window {
    initMap: () => void;
  }
}
window.initMap = initMap;
//dotenv.config();
//console.log(process.env);
export {};
