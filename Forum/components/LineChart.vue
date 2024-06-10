<template>
  <div>
    <canvas id="planet-chart"></canvas>
  </div>
</template>

<script>
import {
  Chart,
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Legend,
  Title,
  Tooltip,
} from 'chart.js'
// import planetChartData from '../planet-data.js'

// Register the required components with Chart.js
Chart.register(
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Legend,
  Title,
  Tooltip
)

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
    const ctx = document.getElementById('planet-chart').getContext('2d')
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
