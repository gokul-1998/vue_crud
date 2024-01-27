<template>
    <div class="container mt-5">
        <div class="card">
            <div class="card-header">
                <h4>Add Students</h4>
            </div>
            <div class="card-body">
                 <div class="mt-3">
                    <label for="">Name</label>
                   <input type="text" v-model="model.student.name" class="form-control"/>
                 </div>
                 <div class="mt-3">
                    <label for="">Course</label>
                   <input type="text" v-model="model.student.course" class="form-control"/>
                 </div>
                 <div class="mt-3">
                    <label for="">Email</label>
                   <input type="text" v-model="model.student.email" class="form-control"/>
                 </div>
                 <div class="mt-3">
                    <label for="">Phone</label>
                   <input type="text" v-model="model.student.phone"  class="form-control"/>
                 </div>
                 <div class="mt-3">
                    <button  type="submit" class="btn btn-primary">Save</button>
                 </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "studentCreate",
    data() {
        return {
            model:{
                student:{
                    name:"",
                    course:"",
                    email:"",
                    phone:""
                }
            }
        };
    },
}
</script>