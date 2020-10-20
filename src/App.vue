<template>
  <div id="app">
    <google-map-loader :map-config="mapConfig" :apiKey="apiKey">
      <template slot-scope="scopeProps">
        <my-position :google="scopeProps.google" :map="scopeProps.map" />
        <markers :google="scopeProps.google" :map="scopeProps.map" />
      </template>
    </google-map-loader>
  </div>
</template>

<script>
import GoogleMapLoader from './components/GoogleMapLoader.vue'
import MyPosition from "./components/MyPosition.vue";
import Markers from "./components/Markers.vue";
import { mapConfig, apiKey } from "@/conf.js";

export default {
  name: 'App',
  components: {
    GoogleMapLoader,
    MyPosition,
    Markers
  },
  data() {
    return {
      mapConfig: mapConfig,
      apiKey: apiKey
    };
  }
}
</script>

<style>
</style>
