const path = require("path");
const fs = require("fs");
const { parse } = require("csv-parse/sync");

// https://zenn.dev/tatsuyasusukida/articles/nodejs-csv-read
const canParse = (data, options) => {
  try {
    parse(data, options);
    return { ok: true, err: null };
  } catch (err) {
    return { ok: false, err };
  }
};

const getRandSerif = () => {
  const source = path.join(__dirname, "./serif.csv");
  const buffer = fs.readFileSync(source);
  const { ok, err } = canParse(buffer);

  if (ok) {
    const rows = parse(buffer);
    const randInt = Math.floor(Math.random() * rows.length + 1);
    const serif = rows[randInt];
    const formattedSerif = `${serif[2]} | ${serif[0]}：${serif[1]}`;
    return formattedSerif;
  } else {
    return `うわぁぁぁ！ ${err}だああ！！`;
  }
};

module.exports = getRandSerif;
