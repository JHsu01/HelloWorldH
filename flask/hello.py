from flask import Flask, render_template, redirect
import flaskBGR as bgr
app = Flask(__name__)
color_to_url  = {
	'yellow': 'https://www.google.com/search?client=firefox-b-1-d&biw=1536&bih=728&tbm=shop&sxsrf=ACYBGNSndi7qh0Hly5NFxSLGTsWfwoPksQ%3A1568559051432&ei=y09-XZD6GZDGsQXWqoPYAw&q=yellow+t+shirt+&oq=yellow+t+shirt+&gs_l=psy-ab-sh.3..0l10.116259.118966.0.120000.15.10.0.5.5.0.200.1260.1j7j1.9.0....0...1c.1.64.psy-ab-sh..2.13.1154....0.iY2F8s6dgq0',
	'gray': 'https://www.google.com/search?client=firefox-b-1-d&biw=1853&bih=953&tbm=shop&ei=p1F-XcjHCcaisAXyuquwDA&q=purdue+gray+sweatshirt&oq=purdue+gray+sweatshirt&gs_l=psy-ab-sh.3...125183.134410.0.134631.41.29.9.3.5.0.159.1853.25j3.28.0....0...1c.1.64.psy-ab-sh..1.23.936...0.0.nWOxX0RC2f8',
	'red': 'https://www.google.com/search?tbm=shop&sxsrf=ACYBGNQ0lBtOLqKytK5BBm2pdL0Zg9oxtg%3A1568559381606&psb=1&x=0&y=0&q=red+polo+&oq=red+polo+&aqs=products-cc..0l5',
	'green': 'https://www.google.com/search?tbm=shop&sxsrf=ACYBGNTU0aG9rM4s1aIxKJaOgWzZu5Mwgg%3A1568560952183&psb=1&x=0&y=0&q=plain+green+shirt&oq=plain+green+shirt&aqs=products-cc..',
	'black': 'https://www.google.com/search?tbm=shop&sxsrf=ACYBGNShRFV9emzWiH7fh4ehRx3MnXP08w%3A1568559285254&psb=1&x=0&y=0&q=columbia+vest&oq=columbia+vest&aqs=products-cc..0l4',
	'blue': 'https://www.google.com/search?tbm=shop&sxsrf=ACYBGNQ2QR_MZI_ra391DSNLK4QuZVRK1Q%3A1568561084545&psb=1&x=0&y=0&q=blue+long+sleeve&oq=blue+long+sleeve&aqs=products-cc..0l10',
	'white': 'https://thedenpop.com/shop-all/purdue-university-skyline-comfort-colors-pocket-t'
}


@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/hello')
def test():
	return 'test'

@app.route('/yellow')
def yellow():
	return redirect(color_to_url['yellow'], code=302)

@app.route('/grey')
def gray():
	return redirect(color_to_url['gray'], code=302)

@app.route('/red')
def red():
	return redirect(color_to_url['red'], code=302)

@app.route('/green')
def green():
	return redirect(color_to_url['green'], code=302)

@app.route('/black')
def black():
	return redirect(color_to_url['black'], code=302)

@app.route('/blue')
def blue():
	return redirect(color_to_url['blue'], code=302)

@app.route('/white')
def white():
	return redirect(color_to_url['white'], code=302)

@app.route('/bgr')
def rgb():
        color = bgr.myFunction()
        return color

