# MX Flex - Email Security and Manipulation Tool

**MX Flex** is an all-round email tool designed to help cybersecurity professionals analyze, manage, and manipulate email security records like SPF, DKIM, and DMARC, as well as perform social engineering engagements and generate homoglyph domains.

![Banner](./banner.jpg)   
> [+] An all-round email tool by D8RH8R [+]

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
  - [Whitehat (Blue Team) Options](#whitehat-blue-team-options)
  - [Blackhat (Red Team) Options](#blackhat-red-team-options)
- [License](#license)

## Features

- **Analyze Domain Records**: Examine SPF, DKIM, and DMARC records for errors or potential security issues.
- **SPF Record Management**: Generate, validate, and optimize SPF records.
- **DKIM Key Generation and Configuration**: Create DKIM key pairs, manage selectors, and check configurations.
- **DMARC Policy Setup and Management**: Generate, update, and get advice on DMARC policies.
- **Automated Testing and Validation**: Perform automated testing on email security configurations.
- **Monitoring and Reporting**: Set up monitoring and reporting for email security.
- **Generate Homoglyph Domains**: Create homoglyph versions of a domain for phishing simulations.
- **Generate IP Logger Link**: Generate IP tracking links for social engineering engagements.
- **Generate Pretexting Messages**: Create and refine social engineering messages using OpenAI's GPT-4.

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package manager)
- ChromeDriver (for Selenium WebDriver) installed and added to your system's PATH

### Step-by-Step Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/mx-flex.git
   cd mx-flex
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *Requirements.txt should include:*

   ```plaintext
   beautifulsoup4
   colorama
   cryptography
   dnspython
   openai
   pyfiglet
   selenium
   ```

4. **Configure OpenAI API Key**

   - Set up your OpenAI API key in the script:
   ```python
   openai.api_key = "your_openai_api_key"  # Replace with your actual OpenAI API key
   ```

5. **Run the Tool**

   ```bash
   python mx_flex.py
   ```

## Usage

After running the tool, you'll be presented with the main menu. Choose an option to either go to the Whitehat (Blue Team) or Blackhat (Red Team) menu, or exit the program.

### Main Menu

```plaintext
=====================================
 What colour hat do you wear today?  
=====================================
1. Whitehat
2. Blackhat
3. Exit
```

## Options

### Whitehat (Blue Team) Options

1. **Analyze Domain Records**
   - Analyze SPF, DKIM, and DMARC records for errors or issues.

2. **SPF Record Management**
   - Generate, validate, and optimize SPF records to improve email security.

3. **DKIM Key Generation and Configuration**
   - Generate DKIM key pairs, manage selectors, and verify DKIM configurations.

4. **DMARC Policy Setup and Management**
   - Generate, update, and get policy advice for DMARC records.

5. **Automated Testing and Validation**
   - Conduct automated tests to validate email security settings.

6. **Monitoring and Reporting**
   - Set up continuous monitoring and reporting for domain email security.

7. **Automated Analysis**
   - Perform an automated analysis of domain email security records using ChatGPT for comprehensive reporting.

8. **Back to Main Menu**
   - Return to the main menu.

9. **Exit**
   - Exit the tool.

### Blackhat (Red Team) Options

1. **Generate Homoglyph Domains**
   - Create homoglyph versions of a domain for phishing simulations and social engineering engagements.

2. **Generate IP Logger Link**
   - Generate IP tracking links to identify the location and other details of a clicked link.

3. **Generate Pretexting Messages**
   - Create pretexting messages for social engineering engagements using pre-defined templates and refine them using OpenAI.

4. **Back to Main Menu**
   - Return to the main menu.

5. **Exit**
   - Exit the tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This tool is designed for authorized use only. It should be used for educational purposes or in a professional environment where you have permission to conduct security testing or social engineering. Unauthorized use of this tool could violate laws and regulations.
