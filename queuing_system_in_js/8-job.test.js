import createPushNotificationsJobs from "./8-job.js";
import kue from "kue";

const queue = kue.createQueue();
