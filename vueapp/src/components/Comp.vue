<template>
  <div>
    <p>Company Data</p>
    <form action="" @submit.prevent="searchTitles()">
        <div class="col-sm-6">
            <input v-model="title" title="" type="text" class="form-control">
            <button type="submit" name="button">Search Title</button>
        </div>
    </form>

    <table class="table table-striped mt-4">
      <thead>
      <tr>
        <th scope="col">ID</th>
        <th scope="col">Title</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="input in titles.edges" :key="input.id">
        <td>{{ input.node.id }}</td>
        <td>{{ input.node.titleName }}</td>
      </tr>
      </tbody>
    </table>

    <form action="" @submit.prevent="searchEmployees()">
      <div class="col-sm-6">
        <input v-model="city" city="" type="text" class="form-control">
        <button type="submit" name="button">Submit</button>
      </div>
    </form>   
    <table class="table table-striped mt-4">
      <thead>
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Title</th>
        <th scope="col">City</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="input in employees.edges" :key="input.id">
        <td>{{ input.node.employeeName }}</td>
        <td>{{ input.node.employeeTitle.titleName }}</td>
        <td>{{ input.node.employeeCity.cityName }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
    export default {
        name: 'CompanyData',
        data(){
            return {
                city: '',
                title: '',
                titles: [],
                employees: []
            }
        },
        methods: {
            getTitles: async function(){
                try {
                    var result = await axios({
                        method: 'POST',
                        url: 'http://127.0.0.1:8000/graphql/',
                        data:{
                            query: `{
                                allTitles {
                                    edges {
                                        node{
                                            id
                                            titleName
                                        }
                                    }
                                }
                            }`
                        }
                    })
                    this.titles = result.data.data.allTitles
                } catch (error){
                    console.error(error)
                }
            },
            getEmployees: async function(){
                try {
                    var result = await axios({
                        method: 'POST',
                        url: 'http://127.0.0.1:8000/graphql/',
                        data:{
                            query: `{
                                allEmployees {
                                    edges {
                                        node{
                                            id
                                            employeeName
                                            employeeTitle{
                                                titleName
                                            }
                                            employeeCity{
                                                cityName
                                            }
                                        }
                                    }
                                }
                            }`
                        }
                    })
                    this.employees = result.data.data.allEmployees
                } catch (error){
                    console.error(error)
                }
            },
            searchEmployees: async function(){
                try {
                    var result = await axios({
                        method: 'POST',
                        url: 'http://127.0.0.1:8000/graphql/',
                        data:{
                            query: `{
                                allEmployees(employeeCity_CityName: "`+this.city+`") {
                                    edges {
                                        node{
                                            id
                                            employeeName
                                            employeeTitle{
                                                titleName
                                            }
                                            employeeCity{
                                                cityName
                                            }
                                        }
                                    }
                                }
                            }`
                        }
                    })
                    this.employees = result.data.data.allEmployees
                } catch (error){
                    console.error(error)
                }
            },
            searchTitles: async function(){
                try {
                    var result = await axios({
                        method: 'POST',
                        url: 'http://127.0.0.1:8000/graphql/',
                        data:{
                            query: `{
                                allTitles(titleName: "`+this.title+`") {
                                    edges {
                                        node{
                                            id
                                            titleName
                                        }
                                    }
                                }
                            }`
                        }
                    })
                    this.titles = result.data.data.allTitles
                } catch (error){
                    console.error(error)
                }
            }
        },
        mounted(){
            this.getTitles();
            this.getEmployees();
        }
    }
</script>

<style lang="scss" scoped>
</style>