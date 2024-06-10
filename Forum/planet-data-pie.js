export const planetChartData = {
    type: "pie",
    data: {
      labels: ["Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4", "Tháng 5", "Tháng 6", "Tháng 7", "Tháng 8"],
      datasets: [
        {
          label: "Số sách thêm vào mỗi tháng",
          data: [0, 0, 1, 2, 79, 82, 27, 14],
          backgroundColor: [
            "rgba(54,73,93,.5)",
            "rgba(71, 183,132,.5)",
            "rgba(255, 0, 0,.5)",
            "rgba(255, 165, 0,.5)",
            "rgba(0, 128, 0,.5)",
            "rgba(0, 0, 255,.5)",
            "rgba(75, 0, 130,.5)",
            "rgba(238, 130, 238,.5)"
          ],
          borderColor: [
            "#36495d",
            "#47b784",
            "#ff0000",
            "#ffa500",
            "#008000",
            "#0000ff",
            "#4b0082",
            "#ee82ee"
          ],
          borderWidth: 3
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        tooltip: {
          enabled: true,
        },
      }
    }
  };
  
  export default planetChartData;
  