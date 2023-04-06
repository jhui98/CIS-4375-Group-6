<script>
import axios from "axios"
export default{
    data() {
        return {
            isoData:[],
        };
    },

    methods:{
        //Get Function for ISO table, used to fill in table
        getISO() {
            const path = `http://localhost:5000/api/iso/all`;
            axios.get(path)
            .then((res) => {
                this.isoData = res.data
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

<template>
    <main class="home-page">
        <h1>Home</h1>
        <p>This is the home page</p>

        <div class="jumbotron vertical center">
            <div class="container">
                
                <div class="row">
                    <div class="col-sm-12">
                        <p> Header</p>
                        <hr><br>

                        <button type="button" class="btn btn-success
                        btn-sm" v-b-modal.iso-modal>Add ISO</button>
                        <br><br>
                        <table class="table table-hover">
                            <!-- Table Head-->
                            <thead>
                                <tr>
                                    <!--Table Head cells-->
                                    <th scope="col">ID</th>
                                    <th scope="col">Name</th>
                                    <th scope="col">Action</th>

                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item, ISO_ID in isoData" :key="item.ISO_ID">
                                    <td> {{item.ISO_ID}} </td>
                                    <td> {{ item.ISO_COMPANY }} </td>
                                    <td> 
                                        <div class="btn-group" role="group">
                                            <button type="button" class="btn btn-info
                                            btn-sm">Update</button>
                                            <button type="button" class="btn btn-danger
                                            btn-sm">Delete</button>
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

    <!-- <b-modal ref="addISOModal" id="iso-modal" title="Add an ISO" >
        <b-form @submit ="onSubmit" @reset="onReset" class="w-100">
            <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
                <b-form-input id="form-title-input"
                type="text"
                v-model="addISOForm.isoName"
                required
                placeholder = "Enter ISO Name">

                </b-form-input>
            </b-form-group>

       
            <button type="submit" varient="primary">Submit</button>
            <button type="reset" varient="primary">Reset</button>
        </b-form>

    </b-modal> -->

</template>