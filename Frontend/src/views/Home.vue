<script>
import axios from "axios"
export default{
    data() {
        return {
            openData:[],
        };
    },

    methods:{
        //Get Function for ISO table, used to fill in table
        getISO() {
            this.openData = [];
            const path = `http://localhost:5000/api/orders/open`;
            axios.get(path)
            .then((resp) => {
                this.openData = resp.data;
            })
            .catch((err) => {
                console.error(err);
            });
        },
    },
    created () {
        this.getISO();
    }
}

</script>

<!--Styling of the Home webpage-->
<style>
@import "bootswatch/dist/flatly/bootstrap.min.css";

* {
  box-sizing: border-box;
}

.column {
  float: left;
  width: 33.33%;
  height: 100px;
  border-style: double;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: border-box;
  clear: both;
}
.delete {
  background-color: #f44336; /* Red */
  border: none;
  color: white;
  padding: 15px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>

<template>
    <main class="home-page">
        <h1>Home</h1>
        <br>
        <h4>All Open Orders are listed below</h4>
    <div class="jumbotron vertical center">
      <div class="container">
        <div class="row">
          <div class="col-sm-12">
            <hr />
            <br />
            <table class="table table-hover">
              <!-- Table Head-->
              <thead>
                <tr>
                  <!--Table Head cells-->
                  <th scope="col">Order #</th>
                  <th scope="col">Order Date</th>
                  <th scope="col">Hardware name</th>
                  <th scope="col">Merchant Name</th>
                  <th scope="col">Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in openData" :key="item.ORDER_ID">
                  <!--Do no show this to user-->
                  <!-- <td>{{ item.order_id }}</td> -->
                  <td>{{ item.ORDER_NUM }}</td>
                  <td>{{ item.ORDER_DATE }}</td>
                  <!-- Searches through all pulled merchants and finds record that matches the item's merchant_id, then returns its name - Thanks Zach :) -->
                  <td>{{ item.HARDWARE_NAME }}</td>
                  <td>{{ item.MERCHANT_NAME }}</td>
                  <td>
                    <div class="btn-group" role="group">
                      <!--Update Button-->
                      <button
                        type="button"
                        class="btn btn-info btn-sm"
                     
                      >
                        Update
                      </button>
                      <!--Delete Button-->
                      <button
                        type="button"
                        class="btn btn-danger btn-sm"
                   
                      >
                        Delete
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
        


    </main>


</template>