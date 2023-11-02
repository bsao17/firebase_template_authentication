const initializeApp = require("firebase/app")

config = {
    "apiKey": process.env.API_KEY,
    "authDomain": process.env.AUTH_DOMAIN,
    "projectId": process.envPROJECT_ID,
    "storageBucket": process.env.STORAGE_BUCKET,
    "messagingSenderId": process.env.MESSAGING_SENDER_ID,
    "appId": process.env.APP_ID,
    "measurementId": process.env.MEASUREMENT_ID,
}

const app = initializeApp()
app.config(config)