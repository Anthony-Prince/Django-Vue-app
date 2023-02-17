<template>
  <div class="app">
    <EmployeesList />
  </div>
</template>

<script>
import EmployeesList from './components/EmployeesList.vue'

export default {
  name: 'App',
  components: {
    EmployeesList,
  }
}
</script>

<style scoped>
</style>