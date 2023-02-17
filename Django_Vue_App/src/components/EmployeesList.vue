<template>
  <div class="content">
    <h1>Employees App</h1>

    <div class="add_form">
      <form v-on:submit.prevent="submitEmployee">
        <input
          type="text"
          class="form-control"
          placeholder="Full Nmae"
          v-model="fullname"
        />
        <input
          type="text"
          class="form-control"
          placeholder="Birth Date"
          v-model="dep"
        />
        <input
          type="text"
          class="form-control"
          placeholder="Department"
          v-model="birthdate"
        />
        <input
          type="text"
          class="form-control"
          placeholder="Salary"
          v-model="salary"
        />
        <button type="submit" class="btn btn-primary">
          {{ isEditing ? "Edit Employee" : "Add Employee" }}
        </button>
      </form>
    </div>

    <div class="list">
      <ul class="list_content">
        <li v-for="employee in employees" :key="employee.id">
          <h4>{{ employee.fullname }}</h4>
          <h4>{{ employee.dep }}</h4>
          <h4>{{ employee.birthdate }}</h4>
          <h4>{{ employee.salary }}</h4>
          <div class="list_buttons">
            <button @click="editEmployee(employee)">Edit</button>
            <button @click="deleteEmployee(employee)">Delete</button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      employees: [],
      fullname: "",
      dep: "",
      birthdate: "",
      salary: "",
      id: "",
      isEditing: false,
    };
  },
  methods: {
    async getEmployee() {
      try {
        await this.$http
          .get(`http://127.0.0.1:8000/api/employees/`)
          .then((response) => {
            this.employees = response.data;
          });
      } catch (error) {
        console.log(error);
      }
    },
    async submitEmployee() {
      try {
        if (!this.isEditing) {
          await this.$http
            .post(`http://127.0.0.1:8000/api/employees/`, {
              fullname: this.fullname,
              dep: this.dep,
              birthdate: this.birthdate,
              salary: this.salary,
            })
            .then((response) => {
              this.employees.push(response.data);
              this.fullname = "";
              this.dep = "";
              this.birthdate = "";
              this.salary = "";
            });
        } else {
          await this.$http
            .put(`http://127.0.0.1:8000/api/employees/${this.id}/`, {
              fullname: this.fullname,
              dep: this.dep,
              birthdate: this.birthdate,
              salary: this.salary,
            })
            .then((response) => {
              let objIndex = this.employees.findIndex((s) => s.id === this.id);
              let tmp = this.employees;
              tmp[objIndex] = response.data;
              this.employees = tmp;
              this.fullname = "";
              this.dep = "";
              this.birthdate = "";
              this.salary = "";
              this.id = "";
              this.isEditing = false;
              this.getEmployee();
            });
        }
      } catch (error) {
        console.log(error);
      }
    },
    async editEmployee(employee) {
      try {
        this.isEditing = true;
        this.fullname = employee.fullname;
        this.dep = employee.dep;
        this.birthdate = employee.birthdate;
        this.salary = employee.salary;
        this.id = employee.id;
      } catch (error) {
        console.log(error);
      }
    },
    async deleteEmployee(employee) {
      if (!confirm("Are you sure?")) {
        return;
      }
      await this.$http.delete(`http://127.0.0.1:8000/api/employees/${employee.id}/`);
      await this.getEmployee();
    },
  },
  created() {
    this.getEmployee();
  },
};
</script>

// apply styling to the component

<style scoped></style>
