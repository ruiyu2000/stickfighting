global.XMLHttpRequest = require("xhr2");

const tf = require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node');

const fetch = require('node-fetch');
const {Image, createCanvas} = require('canvas');
const posenet = require('@tensorflow-models/posenet')

async function run() {
  let img_path = 'http://www.cgriver.com/89246-thickbox/high-quality-3d-human-model-bman0006hd2-o01p05s.jpg';
  let buffer = await fetch(img_path).then(res => res.buffer());
  let img = new Image();
  img.src = buffer;
  const canvas = createCanvas(img.width,img.height);
  canvas.getContext('2d').drawImage(img,0,0);

  const imageScaleFactor = 0.5;
  const flipHorizontal = false;
  const outputStride = 8;
  const multiplier = 0.5;

  const net  = await posenet.load(multiplier);
  const pose = await net.estimateSinglePose(canvas, imageScaleFactor, flipHorizontal, outputStride);
  console.log(pose);
  return pose;
}

run();