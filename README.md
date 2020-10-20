# Map Waypoints Generator
A web application that allows user to submit addresses of 1 pickup point and 1 drop-off point, and then display the waypoints in the map. 

## Goals
1. Get the addresses of pickup and drop-off points from user input and submit them to our Mock API backend.
	- Retry logic when the backend is busy (returns `in progress` response).
	- Should stop requesting when the backend returns error.
	- All errors must be handled.
	- Correct Mock API usage in accordance with the documentation.
2. Display waypoints returned from Mock API on an embedded map.
    - Please use a map provider such as Google Maps, Mapbox, or HERE Maps.
    - Waypoints must be displayed on corresponding latitude and longitude.
    - Each waypoint must show its sequence (e.g. 1, 2, 3, or A, B ,C) and in correct order (using image/icon is allowed).

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
