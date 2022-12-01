// https://discordjs.guide/creating-your-bot/command-deployment.html

// Require the necessary discord.js classes
const { Client, Events, GatewayIntentBits, Collection } = require("discord.js");
const config = require("./config.json");
const fs = require("node:fs");
const path = require("node:path");
const getRandSerif = require("./get-rand-serif");

// https://github.com/discordjs/guide/blob/main/code-samples/creating-your-bot/command-handling/index.js
const client = new Client({
  partials: ["MESSAGE"],
  intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages],
});

client.commands = new Collection();
const commandsPath = path.join(__dirname, "commands");
const commandFiles = fs
  .readdirSync(commandsPath)
  .filter((file) => file.endsWith(".js"));

for (const file of commandFiles) {
  const filePath = path.join(commandsPath, file);
  const command = require(filePath);
  client.commands.set(command.data.name, command);
}

client.once(Events.ClientReady, () => {
  console.log("Ready!");
});

client.on(Events.InteractionCreate, async (interaction) => {
  if (!interaction.isChatInputCommand()) return;

  const command = client.commands.get(interaction.commandName);

  if (!command) return;

  try {
    await command.execute(interaction);
  } catch (error) {
    console.error(error);
    await interaction.reply({
      content: "There was an error while executing this command!",
      ephemeral: true,
    });
  }
});

// client.on(Events.MessageCreate, async (message) => {
client.on(Events.MessageCreate, async (message) => {
  console.log("RUN!");
  if (message.author.bot || message.channel.type === "DM") return;
  console.log("message.content is");
  console.log(message.content);
  const rate = Math.floor(Math.random() * 100);
  if (rate <= 30) {
    client.channels.cache.get("878900170429956156").send(getRandSerif());
  } else {
    client.channels.cache.get("878900170429956156").send(`1d100 = ${rate}`);
  }
});

client.login(config.token);
