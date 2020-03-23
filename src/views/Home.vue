<template>
  <div class="home">
    <canvas width="640" height="500" ref="can" />
    <img style="display: none;" id="vid" :src="imgData">
    <a href="#" @click="cur = 0">1</a>
    <a href="#" @click="cur = 1">2</a>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
  },
  data: function(){
    return{
      cur: 0,
      imgData: null,
      can: null,
      ctx: null
    }
  },
  watch:{
    cur(v){
      this.socket.send(v)
    }
  },
  mounted(){
    let loc = window.location.hostname;
    if(loc == "localhost"){
      loc = "0.0.0.0";
    }
    this.$nextTick(() => {
      this.can = this.$refs.can;
      this.ctx = this.can.getContext('2d');
    })
    this.socket = new WebSocket("ws://"+loc+":9000");
    this.socket.addEventListener('message', (e) => {
      const img = document.getElementById('vid');
      this.imgData = "data:image/png;base64,"+e.data;
      if(this.ctx){
        this.ctx.drawImage(img, 0, 0, 500, 500);
      }
    })

  }
}
</script>
