<template>
  <div>
    <canvas id="planet-chart-pie"></canvas>
  </div>
</template>

<script>
import { Chart, PieController, ArcElement, Tooltip, Legend } from 'chart.js'
// import planetChartData from '../planet-data-pie.js'

// Register the required components with Chart.js
Chart.register(PieController, ArcElement, Tooltip, Legend)

export default {
  name: 'PlanetChart',
  props:{
    planetChartData: {}
  },
  data() {
    return {
      
    }
  },
  mounted() {
    const ctx = document.getElementById('planet-chart-pie').getContext('2d')
    this.createChart(ctx, this.planetChartData)
  },
  methods: {
    createChart(ctx, chartData) {
      return new Chart(ctx, chartData)
    },
  },
}
</script>

<style>
/* Add any custom styles here */
</style>
