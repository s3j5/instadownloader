async function downloadInsta() {
    console.log("BUTTON CLICKED"); // 👈 ye add karo

    let url = document.getElementById("url").value;
    let result = document.getElementById("result");

    if (!url) {
        result.innerHTML = "❌ Please enter link";
        return;
    }

    result.innerHTML = "⏳ Downloading... Please wait";

    try {
        let res = await fetch('/download/instagram', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({url})
        });

        let data = await res.json();

        console.log(data); // 👈 debug

        if (data.status === "error") {
            result.innerHTML = "❌ " + data.message;
            return;
        }

        // result.innerHTML = `
        //     <h3>${data.title}</h3>
        //     <video width="300" controls>
        //         <source src="${data.file_url}">
        //     </video>
        //     <br><br>
        //     <a href="${data.file_url}" download>
        //         <button>⬇ Download Video</button>
        //     </a>
        // `;

        result.innerHTML = `
            <div class="result-card">
                <h3>${data.title}</h3>
                <video controls>
                    <source src="${data.file_url}">
                </video>
                <a href="${data.file_url}" download>
                    <button>⬇ Download</button>
                </a>
            </div>
        `;

    } catch (err) {
        result.innerHTML = "❌ Server error";
    }
}

async function downloadAudio() {
    let url = document.getElementById("url").value;
    let result = document.getElementById("result");

    result.innerHTML = "⏳ Extracting Audio...";

    let res = await fetch('/download/audio', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({url})
    });

    let data = await res.json();

    // result.innerHTML = `
    //     <h3>${data.title}</h3>
    //     <audio controls>
    //         <source src="${data.file_url}">
    //     </audio>
    //     <br><br>
    //     <a href="${data.file_url}" download>
    //         <button>⬇ Download Audio</button>
    //     </a>
    // `;

    result.innerHTML = `
        <div class="result-card">
            <h3>${data.title}</h3>
            <audio controls>
                <source src="${data.file_url}">
            </audio>
            <a href="${data.file_url}" download>
                <button>⬇ Download Audio</button>
            </a>
        </div>
    `;
}