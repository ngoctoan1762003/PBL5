<!-- components/ChartistChart.vue -->
<template>
  <div class="ct-chart"></div>
</template>

<script>
import 'chartist/dist/chartist.min.css';
import Chartist from 'chartist';

export default {
  name: 'ChartistChart',
  props: {
    data: {
      type: Object,
      required: true
    },
    options: {
      type: Object,
      required: false,
      default: () => ({})
    },
    responsiveOptions: {
      type: Array,
      required: false,
      default: () => []
    }
  },
  mounted() {
    // eslint-disable-next-line no-new
    new Chartist.Bar('.ct-chart', this.data, this.options, this.responsiveOptions);
  }
};
</script>

<style scoped>
.ct-chart {
  height: 300px;
}
</style>
