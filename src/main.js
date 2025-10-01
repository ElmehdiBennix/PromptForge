#!/usr/bin/env node
import dotenv from "dotenv";
import chalk from "chalk";
import figlet from "figlet";
import { getProblem } from "./ui/prompt.js";
import { generateExpertPersona, launchGeminiCLI } from "./core/engine.js";

dotenv.config();

async function main() {
  console.log(
    chalk.cyan(figlet.textSync("Gemini Experts", { horizontalLayout: "full" }))
  );

  const problem = await getProblem();

  if (!problem) {
    console.error(chalk.red("No problem description provided."));
    return;
  }

  console.log(chalk.yellow("Generating expert persona..."));
  const expertPersona = await generateExpertPersona(problem);
  console.log(chalk.green("Expert persona generated!"));

  console.log(chalk.yellow("Launching gemini-cli with the expert persona..."));
  launchGeminiCLI(expertPersona, problem);
}

main();
