import inquirer from "inquirer";
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import chalk from "chalk";

export async function getProblem() {
  const argv = yargs(hideBin(process.argv))
    .option("prompt", {
      alias: "p",
      type: "string",
      description: "The problem description",
    })
    .option("interactive", {
      alias: "i",
      type: "boolean",
      description: "Force interactive mode",
    })
    .help().argv;

  const isPiped = !process.stdin.isTTY;

  if (argv.interactive && isPiped) {
    console.error(
      chalk.red(
        "Error: The --interactive flag cannot be used when input is piped from stdin."
      )
    );
    process.exit(1);
  }

  if (argv.prompt) {
    return argv.prompt;
  }

  if (isPiped) {
    let pipedInput = "";
    for await (const chunk of process.stdin) {
      pipedInput += chunk;
    }
    return pipedInput.trim();
  }

  if (argv.interactive || !argv.prompt) {
    const answers = await inquirer.prompt([
      {
        type: "input",
        name: "problem",
        message: "Describe the problem you need to solve:",
      },
    ]);
    return answers.problem;
  }
}
