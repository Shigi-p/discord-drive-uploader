const { SlashCommandBuilder } = require("discord.js");
const getRandSerif = require("../get-rand-serif.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("serif")
    .setDescription("ランダムに迷言を返してくれます"),
  async execute(interaction) {
    await interaction.reply(getRandSerif());
  },
};
