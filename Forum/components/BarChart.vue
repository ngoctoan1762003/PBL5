<template>
  <!-- <Bar
    id="my-chart-id"
    :options="chartOptions"
    :data="chartData"
  /> -->
  <div>
    kkk
  </div>
</template>

<script>
// import { Bar, Chart as ChartJS } from 'vue-chartjs'
// import { Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

export default {
  name: 'BarChart',
//   components: { Bar },
  data() {
    return {
      chartData: {
        labels: ['January', 'February', 'March'],
        datasets: [{ data: [40, 20, 12] }]
      },
      chartOptions: {
        responsive: true
      }
    }
  },
  mounted() {
    // ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  }
}
</script>
