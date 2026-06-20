window.onload = function () {

    document.getElementById("analyzeBtn").onclick = async function () {

        const file = document.getElementById("resume").files[0];

        if (!file) {
            alert("Select a PDF first");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);
        formData.append(
            "job_description",
            document.getElementById("jobDescription").value
        );

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/upload",
                {
                    method: "POST",
                    body: formData
                }
            );

            const text = await response.text();

            document.getElementById("result").innerHTML =
                "<pre>" + text + "</pre>";

        } catch (error) {

            document.getElementById("result").innerHTML =
                "<pre>" + error + "</pre>";
        }
    };
};