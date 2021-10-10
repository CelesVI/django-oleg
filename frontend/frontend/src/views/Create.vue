<template>
  <div id="app">

    <form @submit.prevent="createStudent">
      <div class="form-group row">
        <input type="text" class="form-control col-2 mx-2" placeholder="Name" v-model="student.name">
        <input type="text" class="form-control col-2 mx-2" placeholder="Course" v-model="student.course">
        <input type="text" class="form-control col-2 mx-2" placeholder="Rating" v-model="student.rating">
        <button class="btn btn-success">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>


export default {
  name: 'App',
  data(){
    return {
      student:{
        
      }
    }
  },
  methods: {
    async createStudent(){

      await fetch('http://127.0.0.1:8000/api/students/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
    },  
    
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>