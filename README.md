# stream_kinect

***NOTE***: As of right now this is a personal repository to archive things and keep everything in sync. It's not catered to the public as of yet but if you know what you're doing feel free to poke around. 

This is a repository of a combination of tech to create interactive and immersive streams. As of right now it works best on linux/unix based systems since the old libfreenect python wrappers are rather difficult to compile on windows. If you can do it, please let me know! 

It relies on:

- Microsoft Kinect (1.8) with Libfreenect and NI Mate (until I figure out how to do distance based OSC triggers through libfreenect)
- PSMove Motion controllers with the PSMove API
- OBS through Websockets
- OSC for controlling VCVRack / Blender and NI Mate triggers
- Python 3
- NodeJS
- Vue


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
