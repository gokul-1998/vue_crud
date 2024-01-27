

<template >
   <div class="container">
   <div class="card">
   <div class="card-header">
    <h4>Students
    <RouterLink   to="/students/create" class="btn btn-primary float-end">Add Student</RouterLink>
    </h4>

    
   </div>
   <div class="card-body">
      <table class="table table-bordered">
         <thead>
            <tr>
               <th>Id</th>
               <th>Name</th>
               <th>Course</th>
               <th>Email</th>
               <th>Phone</th>
               
               <th>Created At</th>
               <th>Action</th>
            </tr>
         </thead>
         <tbody v-if="this.students.length>0">
            <tr v-for="(student,index) in this.students" :key="index">
               <td>{{ student.id }}</td>
               <td>{{ student.name }}</td>
               <td>{{ student.course }}</td>
               <td>{{ student.email }}</td>
               <td>{{ student.phone }}</td>
               <td>{{ student.created_at }}</td>
               <td>
                  <RouterLink  to="/" class="btn btn-success ">Edit</RouterLink>
                  <button class="btn btn-danger float-end">Delete</button>
               </td>

            </tr>
         </tbody>
         <tbody v-else>
            <tr>
               <td colspan="7" class="text-center">Loading...</td>
            </tr>
         </tbody>

      </table>
   </div>
</div>

   </div>

  </template>
  
   <script>
   import axios from "axios";
   export default {
      name: "students",
      data() {
         return {
            students: [],
         };
      },
      mounted() {
         this.getStudents();
      },
      methods: {
         getStudents() {
            axios.get("http://localhost:5000/api/students").then((response) => {
               this.students = response.data.students;
               console.log(response);
            });
         },
         deleteStudent(id) {
            axios.delete(`/students/${id}`).then((response) => {
               this.getStudents();
            });
         },
      },
   };
   </script>