<template>
  <div id="app">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-4">
          <form :onsubmit="submitForm">
            <div class="form-group">
              <label for="startingLocation">Starting Location</label>
              <v-select label="name" :filterable="false" :options="options" @search="onSearch">
                <template slot="no-options">
                  Type location...
                </template>
                <template slot="option" slot-scope="option">
                  <div class="d-center"> 
                    {{ option.name }}
                    </div>
                </template>
                <template slot="selected-option" slot-scope="option">
                  <div class="selected d-center"> 
                    {{ option.name }}
                  </div>
                </template>
              </v-select>
            </div>
            <div class="form-group">
              <label for="dropoffPoint">Drop-off point</label>
              <input type="text" class="form-control" id="dropoffPoint" placeholder="Type location...">
            </div>
            <div v-if="submitted" class="card info">
              <div class="card-body">
                <div>Total Distance: {{totalDistance}}</div>
                <div>Total Time: {{totalTime}}</div>
              </div>
            </div>
            <div v-if="error" class="alert alert-danger" role="alert">
              {{error}}
            </div>
            <button v-if="submitted" type="submit" class="btn btn-primary">Re-Submit</button>
            <button v-else type="submit" class="btn btn-primary">Submit</button>
            <button type="reset" class="btn btn-secondary">Reset</button>
          </form>
        </div>
        <div class="col-sm-8">
          <google-map-loader :map-config="mapConfig" :apiKey="apiKey">
            <template slot-scope="scopeProps">
              <markers :google="scopeProps.google" :map="scopeProps.map" />
            </template>
          </google-map-loader>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import GoogleMapLoader from './components/GoogleMapLoader.vue'
import Markers from "./components/Markers.vue";
import { mapConfig, apiKey } from "@/conf.js";
import axios from 'axios'
import _ from 'lodash';

/**
 * Search map: https://maps.googleapis.com/maps/api/place/findplacefromtext/json\?input\=Museum%20of%20Contemporary%20Art%20Australia\&inputtype\=textquery\&fields\=photos,formatted_address,name,rating,opening_hours,geometry\&key\=AIzaSyBtuCzmWiqghKRfiHDs-uW5uO8bQkK51ic
 */

export default {
  name: 'App',
  components: {
    GoogleMapLoader,
    Markers
  },
  data() {
    return {
      mapConfig: mapConfig,
      apiKey: apiKey,
      submitted: true,
      totalDistance: 0,
      totalTime: 0,
      error: '',
      options: []
    };
  },
  methods: {
    submitForm (e) {
      e.preventDefault();
    },
    onSearch(search, loading) {
      loading(true);
      this.search(loading, search, this);
    },
    search: _.debounce((loading, search, vm) => {
      axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
      axios.get(
        `https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=${escape(search)}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyBtuCzmWiqghKRfiHDs-uW5uO8bQkK51ic`
      ).then(res => {
        res.json().then(json => (vm.options = json.items));
        loading(false);
      });
    }, 350)
  }
}
</script>

<style>
#app {
  padding: 15px 0;
}
button {
  margin: 0 10px 10px 0 !important;
}
.info {
  margin-bottom: 20px;
}
</style>
