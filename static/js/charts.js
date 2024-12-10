const dataset = JSON.parse(document.currentScript.dataset.data);

const ctxProductsPercentage = document.getElementById('products-percentage');
const ctxProductsQuantity = document.getElementById('products-quantity');
const ctxProductsPerSupplier = document.getElementById('products-per-supplier');
const ctxProductsPerSupplierPercentage = document.getElementById('products-per-supplier-percentage');

const productPercentage = dataset.productPercentage;
const productPercentageLabels = productPercentage.labels;
const productPercentageData = productPercentage.data;

const productQuantity = dataset.productQuantity;
const productQuantityLabels = productQuantity.labels;
const productQuantityData = productQuantity.data;

const productsPerSupplier = dataset.productsPerSupplierQuantity;
const productsPerSupplierLabels = productsPerSupplier.labels;
const productsPerSupplierData = productsPerSupplier.data;

const productsPerSupplierPercentage = dataset.productsPerSupplierPercentage;
const productsPerSupplierPercentageLabels = productsPerSupplierPercentage.labels;
const productsPerSupplierPercentageData = productsPerSupplierPercentage.data;


new Chart(ctxProductsPerSupplierPercentage, {
    type: 'pie',
    plugins: [ChartDataLabels],
    data: {
        labels: productsPerSupplierPercentageLabels,
        datasets: [
            {
                label: 'Produtos por fornecedor (%)',
                data: productsPerSupplierPercentageData,
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Porcentagem de produtos por fornecedor'
            },
            datalabels: {
                font: {
                    size: 16,
                },
                formatter: function (value, context) {
                    return value + '%';
                }
            }
        }
    },
});
new Chart(ctxProductsPercentage, {
    type: 'pie',
    plugins: [ChartDataLabels],
    data: {
        labels: productPercentageLabels,
        datasets: [
            {
                label: 'Produtos por categoria (%)',
                data: productPercentageData,
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Porcentagem de produtos por categoria'
            },
            datalabels: {
                font: {
                    size: 16,
                },
                formatter: function (value, context) {
                    return value + '%';
                }
            }
        }
    },
});
new Chart(ctxProductsQuantity, {
    type: 'bar',
    plugins: [ChartDataLabels],
    data: {
        labels: productQuantityLabels,
        datasets: [
            {
                label: 'Produtos por categoria',
                data: productQuantityData,
            },
        ],
    },
    options: {
        backgroundColor: "rgba(0, 89, 84, 0.5)",
        borderColor: "#005954",
        borderWidth: 1,
        borderRadius: "6",
        borderSkipped: false,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "Quantidade de produtos por categoria",
            },
            datalabels: {
                font: {
                    size: 16,
                },
            }
        }
    }
});
new Chart(ctxProductsPerSupplier, {
    type: 'bar',
    plugins: [ChartDataLabels],
    data: {
        labels: productsPerSupplierLabels,
        datasets: [
            {
                label: 'Produtos por fornecedor',
                data: productsPerSupplierData,
            }
        ],
    },
    options: {
        backgroundColor: "rgba(0, 89, 84, 0.5)",
        borderColor: "#005954",
        borderWidth: 1,
        borderRadius: "6",
        borderSkipped: false,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "Quantidade de produtos por fornecedor",
            },
            datalabels: {
                font: {
                    size: 16,
                },
            }
        }
    }
});
