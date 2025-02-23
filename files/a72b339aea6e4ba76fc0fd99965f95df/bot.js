const puppeteer = require('puppeteer');

async function admin(url) {
    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-web-security', '--ignore-certificate-errors', '--disable-setuid-sandbox'],
        headless: true,
    });
    const page = await browser.newPage();

    let saw_popup = false;
    page.on('dialog', async (dialog) => {
        saw_popup = true;
        await dialog.accept();
    });
    
    try {
        await page.goto(url, {
            waitUntil: 'networkidle0'
        });
        await new Promise((resolve, reject) => setTimeout(resolve, 500));
    } catch(e) {
        console.error(e);
    }
    finally {
        await page.close();
        await browser.close();
    }

    return saw_popup;
}

module.exports.admin = admin;