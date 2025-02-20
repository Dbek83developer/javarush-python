function processData() {
    try {
        console.log("Processing data");
    } finally {
        console.log("Cleanup resources");
    }
}

processData();