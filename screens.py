getPermissionAsync = async () => {
    if (Platform.OS !== "web") {
        const { status } = await Permissions.askAsync(Permissions.CAMERA_ROLL);
        if ( status !== "granted") {
            alert("Sorry, we need camera roll permissions to make this work!")
        }
    }
};

uploadImage = async (uri) => {
    const data = new FormData();
    let filename = uri.spilt("/")[uri.spilt("/").length - 1]
    let type = iamge/{uri.spilt('.')[uri.spilt('.').length - 1]}
    const fileTopUpload = {
        uri: uri,
        name: filename,
        type: type,
    };
    data.appened("digit", fileTopUpload);
    fetch("https://f292a3137990.ngrok.io/predict-digit", {
        method: "POST"
        body: data,
        headers: {
            "contents-type": multipart/form-data
        },
    })
      .then((response) => response.json())
      .then((result) => {
          console.log("Success:", result);
      })
      .catch((error) => {
          console.error("Error:", error)
      });
}