#!/usr/bin/env python3
"""Generates public/*.html from the copy below. Run: python3 build.py"""
import os, sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-marcgray/d55a993a-88e8-4ab4-bdd1-3cd1fff14d51/scratchpad/nikki-canvas")
ROOT = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(ROOT, "public")

WIDE = [480, 800, 1200, 1600]

# ---------------- FAQ content ----------------
MIN_Q = ("Is there a minimum number of people?", "Yes. A retreat books at five. Get five people together, pick a weekend, and it's on.")
REFUND_Q = ("What if someone has to cancel?", "Once a weekend is booked, it's booked. There are no refunds, so get the five confirmed before booking.")
COST_Q = ("What does a weekend cost?", "Every weekend is priced for the group. Headcount, the venue, and what the room needs all move the number, so the quote comes after a quick conversation and lands in the proposal.")
WHERE_Q = ("Where is it?", "Every retreat happens at a venue picked for that weekend, somewhere in Arkansas. The proposal names the place, and the details come with the booking.")
RULES_Q = ("What are the house rules?", "Every venue has its own. Check-in, quiet hours, parking, pets, all of it comes from the property and gets passed along in the proposal so nothing is a surprise.")
FOOD_Q = ("Is food included?", "Snacks and drinks, yes. Nikki stocks the weekend with what's listed in the proposal. Meals work like the venue: catering is arranged for that weekend, and the proposal says what's on the table and when.")
SLEEP_Q = ("Do we sleep there?", "Depends on the venue. Some retreats are at a house with beds for everyone. Some are at a workspace with lodging nearby. The proposal says which.")

FAQ = {
"hobby": [MIN_Q, COST_Q,
  ("What should I bring to a quilting or craft retreat?", "The project, the machine, and the tools you actually use. What Nikki sets up, tables, lighting, ironing and cutting stations, is listed in the proposal so nothing gets packed twice."),
  ("Do I have to bring my own sewing machine?", "Yes. Bring the machine you know. There will be a table, an outlet, and light waiting for it."),
  ("Can I come by myself?", "Retreats book at five, so bring the guild, the sewing circle, or four friends who've been meaning to. Solo quilters get on the list and hear first when an open weekend has room."),
  ("Is there a schedule or a class?", "Only if the group wants one. Nikki plans the weekend around the room: open sewing the whole time, one demo on Saturday, or whatever the group asks for."),
  FOOD_Q, SLEEP_Q, RULES_Q, REFUND_Q],
"gaming": [
  ("What can we play?", "Anything that fits on a table. Warhammer, Magic, D&amp;D, Pathfinder, board games, whatever the group brings."),
  MIN_Q, COST_Q,
  ("Do you provide tables and terrain?", "Nikki sets up the tables and whatever the group needs for its game, as listed in the proposal. Bring the terrain the campaign depends on and say so up front, so the room is ready for it."),
  ("Is there a painting station?", "If the group wants one, it goes in the proposal: light, water, and drying space. Bring the paints and the army."),
  ("Can a game stay set up overnight?", "Depends on the venue, and most will let a table sit. Say it matters and Nikki picks a place where the game can stay up until breakfast."),
  ("What about food during a long game?", "Snacks and drinks are stocked so nobody has to leave the table. Catering works like the venue: arranged for that weekend, timed around the game, and spelled out in the proposal."),
  SLEEP_Q, RULES_Q, REFUND_Q],
"corporate": [
  ("How many people can a corporate retreat hold?", "Retreats run for teams of five or more. Say the headcount up front and Nikki picks a venue that fits it."),
  ("What's included?", "A venue picked for the team, the room set to the agenda, snacks and drinks stocked, a run-of-show, and Nikki on site running the clock. Catering and lodging are arranged per retreat and spelled out in the proposal."),
  ("What does a corporate retreat cost?", "Every retreat is built and priced for the team. Headcount, length, venue, and the agenda all shape it, so pricing comes with the proposal."),
  ("Can we bring our own agenda or facilitator?", "Yes. The team owns the content. Nikki owns the logistics and the clock."),
  ("Is there AV?", "Depends on the venue. Say what the agenda needs, projector, screens, whiteboards, wifi, and Nikki picks a place that has it or brings it in. It's all in the proposal."),
  ("Do you offer group training or team building?", "Not personally. I run the retreat. I do have a few facilitators I collaborate with all the time, and if the team wants training or team building built into the weekend, say so and I'll recommend a few."),
  ("What do people do in the evenings?", "Whatever they want. Game night, a craft workshop, or nothing at all. No trust falls."),
  ("How far ahead should we book?", "As early as the calendar allows. A retreat is planned like a production, and the run-of-show takes a few weeks to build."),
  ("Where is it?", "At a venue picked for the team, somewhere in Arkansas. The proposal names the place."),
  REFUND_Q],
"private": [MIN_Q,
  ("How does booking work?", "One organizer picks the weekend and becomes the single point of contact. Nikki sends the proposal, the organizer says yes, and everyone else just shows up."),
  ("What does a private weekend cost?", "Every private weekend is priced for the group. Headcount, the venue, and the setup all move the number, so the quote follows a quick conversation with the organizer."),
  ("Do we get the whole place?", "Yes. A private booking is the group's weekend. Nobody else is on the calendar."),
  ("Can the group mix hobbies?", "Yes. Quilters at one table, painters at another, a board game at a third."),
  ("Are dietary needs handled?", "The organizer sends the group's needs ahead of time, and the snack list and the catering in the proposal are built around them."),
  ("How long is the weekend?", "Most run Friday afternoon to Sunday afternoon, but the group picks. The proposal sets the dates and times."),
  SLEEP_Q, RULES_Q, REFUND_Q],
}

NAV = [("hobby-retreats.html","Hobby Retreats","c-marigold"),("gaming-getaways.html","Gaming Getaways","c-pink"),("corporate-retreats.html","Corporate Retreats","c-sky"),("private-groups.html","Private Groups","c-mint"),("index.html#nikki","Nikki",""),("faq.html","FAQ","")]

FONT_CSS = """@font-face{font-family:'Fraunces';font-style:normal;font-weight:800;font-display:swap;src:url(assets/fonts/fraunces-800.woff2) format('woff2')}
@font-face{font-family:'Karla';font-style:normal;font-weight:400 800;font-display:swap;src:url(assets/fonts/karla-latin.woff2) format('woff2')}
"""
def head(title, desc, canonical, hero_name=None, hero_sizes="(max-width: 900px) 100vw, 54vw"):
    css = open(os.path.join(PUB, "styles.css")).read()
    pre = ""
    if hero_name:
        srcset = ", ".join(f"assets/img/{hero_name}-{x}.webp {x}w" for x in (WIDE + [1920] if hero_name == "craft-friends" else WIDE))
        pre = f'<link rel="preload" as="image" imagesrcset="{srcset}" imagesizes="{hero_sizes}" fetchpriority="high">\n'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#FFF4E3">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
{pre}<link rel="preload" href="assets/fonts/fraunces-800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/karla-latin.woff2" as="font" type="font/woff2" crossorigin>
<style>{FONT_CSS}{css}</style>
</head>
<body>
"""

HEIGHTS = {"craft-friends": 900, "dice": 1201}
def img(name, alt, widths=WIDE, sizes="100vw", cls="", w=1600, h=1067, lazy=True, style=""):
    h = HEIGHTS.get(name, h) if w == 1600 else h
    if name == "craft-friends": widths = list(widths) + [1920]
    srcset = ", ".join(f"assets/img/{name}-{x}.webp {x}w" for x in widths)
    prio = 'loading="lazy" decoding="async"' if lazy else 'fetchpriority="high" decoding="async"'
    st = f' style="{style}"' if style else ""
    return f'<img class="{cls}" src="assets/img/{name}-{widths[-1]}.webp" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" {prio}{st}>'

def nav(active):
    links = "".join(f'<li><a href="{h}"{" class=active" if h==active else ""}>{l}</a></li>' for h,l,_ in NAV)
    return f"""<header class="nav">
<div class="wrap nav-inner">
<a class="brand display" href="index.html">Freckle Flower</a>
<button class="nav-toggle" aria-expanded="false" aria-controls="menu" aria-label="Menu"><span></span><span></span><span></span></button>
<nav id="menu" class="menu"><ul>{links}<li><a class="btn btn-accent" href="index.html#book">Book a Weekend</a></li></ul></nav>
</div>
</header>
<main>
"""

def footer():
    links = "".join(f'<a href="{h}">{l}</a>' for h,l,_ in NAV)
    return f"""</main>
<footer class="footer">
<div class="wrap footer-inner">
<div><div class="display footer-brand">Freckle Flower Event Planning</div><div>Weekend retreats in Arkansas. [Email] · [Phone] · Arkansas</div></div>
<nav class="footer-links">{links}</nav>
<div>© 2026 Freckle Flower Event Planning</div>
</div>
</footer>
<script src="script.js"></script>
</body>
</html>
"""

def hero(img_name, alt, eyebrow, h1, sub, cta1, cta2, shadow="marigold", pos="center 40%", tag="h1", variant=""):
    sizes = "100vw" if variant else "(max-width: 900px) 100vw, 54vw"
    img_tag = img(img_name, alt, cls="hero-img", sizes=sizes, lazy=False, style=f"object-position: {pos}")
    return f"""<section class="hero {variant}">
{img_tag}
<div class="wrap"><div class="card hero-card shadow-{shadow}">
<span class="eyebrow">{eyebrow}</span>
<{tag} class="display hero-title">{h1}</{tag}>
<p class="lead">{sub}</p>
<div class="btn-row">{cta1}{cta2}</div>
</div></div>
</section>
"""

def btn(href, label, cls="btn-accent"):
    return f'<a class="btn {cls}" href="{href}">{label}</a>'

def stakes(h2, paras, color="rust"):
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return f"""<section class="band band-peach"><div class="wrap two-col">
<h2 class="display text-{color}">{h2}</h2><div class="prose">{ps}</div>
</div></section>
"""

SHADOWS = ["marigold","mint","pink","sky","coral","marigold"]
def included(h2, items):
    cards = "".join(f'<div class="card shadow-{SHADOWS[i%6]}"><h3 class="display">{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(items))
    return f"""<section class="band"><div class="wrap">
<h2 class="display">{h2}</h2><div class="grid grid-3">{cards}</div>
</div></section>
"""

def who(h2, text):
    return f"""<section class="band band-mint"><div class="wrap two-col">
<h2 class="display">{h2}</h2><div class="prose"><p>{text}</p></div>
</div></section>
"""

def faq_items(items):
    return "".join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q,a in items)

def faq_section(h2, items):
    return f"""<section class="band"><div class="wrap">
<h2 class="display">{h2}</h2><div class="faq-grid">{faq_items(items)}</div>
</div></section>
"""

def cta_band(h2, label):
    return f"""<section id="book" class="band band-coral"><div class="wrap cta-inner">
<h2 class="display">{h2}</h2><a class="btn btn-ink" href="mailto:[Email]?subject=Booking%20a%20weekend">{label}</a>
</div></section>
"""

def write(name, html):
    with open(os.path.join(PUB, name), "w") as f: f.write(html)
    print("wrote", name)

def service(fname, title, desc, key, img, alt, eyebrow, h1, sub, cta1, cta2, st_h2, st_ps, inc, who_h2, who_text, faq_h2, cta_h2, cta_label, shadow, pos="center 40%"):
    html = head(title, desc, fname, hero_name=img) + nav(fname) + hero(img, alt, eyebrow, h1, sub, btn("#book", cta1), btn("faq.html", cta2, "btn-outline"), shadow, pos) \
        + stakes(st_h2, st_ps) + included("What's included", inc) + who(who_h2, who_text) + faq_section(faq_h2, FAQ[key]) + cta_band(cta_h2, cta_label) + footer()
    write(fname, html)

service("hobby-retreats.html", "Quilting, Sewing, and Craft Retreats in Arkansas | Freckle Flower Event Planning",
  "Weekend quilting, sewing, scrapbooking, and craft retreats in Arkansas. A venue picked for the weekend, tables set, snacks stocked. Books at five people.",
  "hobby", "hero-sewing", "A woman smiling at her sewing machine in a bright studio",
  "Quilting, sewing, and craft retreats in Arkansas", "Forty-eight hours with the project.",
  "Weekend retreats in Arkansas for quilters, sewists, scrapbookers, knitters, and anyone with a craft that keeps losing to the calendar. A venue picked for the weekend, tables set, snacks stocked, and a room full of people who get it.",
  "Book a Craft Weekend", "Read the FAQ",
  "The stash grows. The finished pile doesn't.",
  ["Every quilter knows the project that has been \"almost done\" for two years, and every one of them knows exactly why. An hour on a Tuesday night is enough to get the machine out and put it away again.",
   "A whole weekend is a different thing. The machine stays out. The cutting mat stays on the table. The project moves."],
  [("A venue picked for the weekend","Nikki finds the place in Arkansas that fits the group: good light, big tables, room to spread out."),
   ("Setup done before anyone arrives","Tables, lighting, ironing and cutting stations, laid out the way the proposal says."),
   ("Snacks and drinks, stocked","Nikki brings them, as listed in the proposal. The coffee does not run out."),
   ("Catering, arranged per weekend","Meals work like the venue. Catering is set up for that retreat and the proposal says what's on the table and when."),
   ("Nikki on site","One person running the weekend so nobody in the group has to."),
   ("The proposal","One document with the venue, what's included, and the house rules. Read it once and relax.")],
  "Who comes",
  "Solo quilters who want a weekend alone with the machine. Guilds who want the retreat without one member doing all the work. Scrapbookers with three years of photos in a box. Knitters, crocheters, cross-stitchers, anyone with a hobby that fits on a table. Nobody has to be good at it. Nobody has to finish anything. The weekend counts either way.",
  "Quilting and craft retreat questions", "The project has waited long enough.", "Book a Craft Weekend", "marigold", "70% 40%")

service("gaming-getaways.html", "Tabletop Gaming Retreats in Arkansas | Freckle Flower Event Planning",
  "Weekend tabletop gaming getaways in Arkansas for Warhammer, Magic, D&D, and board game groups. The venue, the tables, and the snacks are handled. Books at five.",
  "gaming", "boardgame", "Four friends leaning over a board game at a wooden table",
  "Tabletop gaming retreats in Arkansas", "The campaign finally gets past session three.",
  "Weekend getaways in Arkansas for tabletop gamers. Warhammer, Magic, D&amp;D, board games, whatever the group plays. The venue, the tables, and the snacks are handled. The only thing anyone has to bring is the army.",
  "Book a Gaming Weekend", "Read the FAQ",
  "Six adults. Six calendars. One campaign.",
  ["Every gaming group has the same problem. A campaign that meets once every two months when it meets at all. The army is half painted. The deck hasn't been sleeved. The board game that takes four hours never comes out because nobody has four hours.",
   "A weekend fixes the math. Two full days, everyone in the same room, and nothing else on the calendar."],
  [("A venue picked for the game","Room for the tables, light to see the dice, and a host who doesn't mind a game running late."),
   ("Tables set for the campaign","Whatever the group's game needs, set up before anyone arrives, as listed in the proposal."),
   ("A painting station if the group wants one","Light, water, and drying space. Bring the paints and the army."),
   ("Snacks and drinks, stocked","Nikki brings them, as listed in the proposal. Nobody leaves the table for a run."),
   ("Catering around the game","Arranged for that weekend, timed to the session, and spelled out in the proposal. Never in the middle of a turn."),
   ("The proposal","One document with the venue, what's included, and the house rules.")],
  "Who comes",
  "Established groups who want a full weekend together for once. Solo players who want to find a table. Painters who want two uninterrupted days at the bench. Anyone who has said \"we should really play more\" and meant it.",
  "Gaming weekend questions", "Roll for a whole weekend.", "Book a Gaming Weekend", "pink", "center 45%")

service("corporate-retreats.html", "Corporate Retreats in Arkansas | Freckle Flower Event Planning",
  "Corporate retreats in Arkansas planned and run by a twenty-year theatre production veteran. A venue that fits the team, a room set to the agenda, and a schedule that holds.",
  "corporate", "corporate", "A team of four working through sticky notes on a glass wall",
  "Corporate retreats in Arkansas", "An offsite run like opening night.",
  "Corporate retreats in Arkansas, planned and run by a twenty-year theatre production veteran. A venue that fits the team, a room set to the agenda, and a schedule that holds.",
  "Request a Proposal", "Read the FAQ",
  "Most offsites get planned by whoever drew the short straw.",
  ["The venue gets booked late, the agenda slips by lunch, and the team spends more time finding the room than using it. Everyone goes home tired, and the one thing on the agenda that mattered never got its hour.",
   "A retreat is a production. There are a hundred moving parts, a hard deadline, and a curtain that goes up whether every piece is ready or not. Twenty years in theatre is twenty years of getting it ready anyway."],
  [("A venue picked for the team","Sized to the headcount, quiet enough to think, close enough to get to."),
   ("The room set to the agenda","Main room and breakouts arranged for the plan, and checked before the team arrives."),
   ("Snacks and drinks, stocked","Nikki brings them, as listed in the proposal. The coffee does not run out."),
   ("A run-of-show","Built with the organizer ahead of time and managed on site by Nikki, minute by minute."),
   ("AV that matches the agenda","Say what the plan needs and Nikki picks a venue that has it or brings it in."),
   ("Evenings without trust falls","Game night, a craft workshop, or nothing at all. The team picks.")],
  "Who books",
  "Teams of five or more. Leadership offsites, planning sessions, annual kickoffs, and the small-company retreat where the owner would rather not be the one running it.",
  "Corporate retreat questions", "The agenda holds. The coffee holds. The team goes home with the thing done.", "Request a Proposal", "sky")

service("private-groups.html", "Private Group Retreats in Arkansas | Freckle Flower Event Planning",
  "Private weekend bookings in Arkansas for quilt guilds, gaming groups, clubs, and friend groups. One organizer, one point of contact, the whole weekend to yourselves.",
  "private", "party-color", "Five friends laughing as a confetti popper goes off",
  "Private group retreats in Arkansas", "Bring the group. Skip the group text.",
  "Private weekend bookings in Arkansas for quilt guilds, gaming groups, clubs, and friend groups who want a retreat without one person doing all the planning.",
  "Book a Private Weekend", "Read the FAQ",
  "Every group has one person who plans everything.",
  ["She finds the rental, collects the money, makes the grocery list, and spends the weekend she planned making sure everyone else is having a good one. Eventually she stops volunteering, and the group stops going anywhere.",
   "A private booking gives that person a weekend off too. One point of contact handles the logistics. The organizer gets to be a guest."],
  [("The group's own weekend","A venue picked for the group, and nobody else on the calendar."),
   ("Setup for the group's thing","Sewing tables, gaming tables, craft stations, or a mix. Ready before anyone arrives."),
   ("Snacks and drinks, stocked","Nikki brings them, built around the needs the organizer sends ahead."),
   ("Catering, arranged per weekend","Meals work like the venue. Set up for that retreat, built around the group, and spelled out in the proposal."),
   ("One point of contact","Nikki handles the logistics from proposal to checkout, so the organizer gets to be a guest."),
   ("Five or more","Private weekends book at five people. Ask about larger groups.")],
  "Who books",
  "Quilt guilds and sewing circles. Gaming groups. Book clubs, scrapbook crops, girls' weekends with a project, church craft groups, anyone with a standing group and a planner who is tired.",
  "Private group questions", "The group is ready. The planner is tired. Book the weekend.", "Book a Private Weekend", "mint")

# ---------------- FAQ page ----------------
def faq_block(anchor, img_name, alt, h2, items, pos="center 45%"):
    return f"""<section id="{anchor}" class="band"><div class="wrap">
{img(img_name, alt, cls="faq-img shadow-marigold", sizes="(max-width: 1232px) calc(100vw - 32px), 1200px", w=1600, h=(1201 if img_name=="dice" else 1067), style=f"object-position: {pos}")}
<h2 class="display">{h2}</h2><div class="faq-grid">{faq_items(items)}</div>
</div></section>
"""
faq_html = head("FAQ | Freckle Flower Event Planning", "Everything people ask before booking a hobby, gaming, corporate, or private group retreat in Arkansas.", "faq.html") + nav("faq.html") + """<section class="band band-peach"><div class="wrap">
<span class="eyebrow">Questions</span>
<h1 class="display page-title">Everything people ask before they book.</h1>
<p class="lead">Every retreat books at five people, happens at a venue picked for that weekend somewhere in Arkansas, and comes with a proposal that spells out what's included. Pick a weekend type below.</p>
<div class="jump">
<a class="btn c-marigold" href="#hobby">Hobby Retreats</a>
<a class="btn c-pink" href="#gaming">Gaming Getaways</a>
<a class="btn c-sky" href="#corporate">Corporate Retreats</a>
<a class="btn c-mint" href="#private">Private Groups</a>
</div>
</div></section>
""" + faq_block("hobby","hero-sewing","A woman smiling at her sewing machine","Hobby Retreats",FAQ["hobby"],"70% 40%") \
  + faq_block("gaming","dice","Polyhedral dice and painted miniatures on a fantasy map","Gaming Getaways",FAQ["gaming"]) \
  + faq_block("corporate","corporate","A team working through sticky notes on a glass wall","Corporate Retreats",FAQ["corporate"]) \
  + faq_block("private","party-color","Friends laughing as confetti falls","Private Groups",FAQ["private"]) + footer()
write("faq.html", faq_html)

# ---------------- Home ----------------
home = head("Freckle Flower Event Planning | Weekend Retreats in Arkansas", "Weekend retreats in Arkansas for people who have something they love and no time to do it. Hobby, gaming, corporate, and private group weekends. Books at five.", "index.html", hero_name="craft-friends", hero_sizes="100vw") + nav("index.html") \
 + hero("craft-friends", "Three friends laughing at a craft table covered in watercolor supplies, one holding up her painting", "Weekend retreats in Arkansas",
        'The hobby gets a <span class="text-rust">whole</span> weekend.',
        "Weekend retreats in Arkansas for people who have something they love and no time to do it. A venue picked for the weekend, snacks stocked, setup done, and a room full of people who came for the same reason. Nothing on the schedule but the thing itself.",
        btn("#book","Book a Weekend"), btn("faq.html","Read the FAQ","btn-outline"), "marigold", "center 38%", variant="hero-wide") \
 + stakes("Most hobbies die of scheduling.", ["The machine sits in the closet. The army stays half painted. The fabric stash grows and the finished quilts don't. Nobody decides to quit. Work fills the weeknights, family fills the weekends, and another season goes by with the good stuff still in the box.",
   "<strong>Two out of three adults say they wish they had more time for a hobby.</strong> Most of them are waiting for the time to show up on its own. It doesn't."]) \
 + f"""<section class="party">
<div class="party-media" aria-hidden="true">
<img class="party-poster" src="assets/img/group-poster-1280.webp" srcset="assets/img/group-poster-800.webp 800w, assets/img/group-poster-1280.webp 1280w" sizes="100vw" width="1280" height="720" alt="" loading="lazy" decoding="async">
<video class="party-video" muted playsinline preload="none" data-src="assets/group-720.mp4" data-src-small="assets/group-540.mp4"></video>
<video class="party-video" muted playsinline preload="none" data-src="assets/craft-720.mp4" data-src-small="assets/craft-540.mp4"></video>
</div>
<div class="wrap"><div class="card party-card shadow-coral">
<span class="eyebrow">The good part</span>
<h2 class="display">Two days without a to-do list.</h2>
<p class="lead">Time, space, and people who get it. Everything else is handled before anyone walks in.</p>
</div></div>
</section>
<section class="band"><div class="wrap">
<div class="grid grid-3">
<div class="card shadow-marigold"><svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg><h3 class="display">Time.</h3><p>Two full days with no meals to cook, no errands to run, and no one asking where anybody is. Morning to whenever.</p></div>
<div class="card shadow-mint"><svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 10h18M8 22h8M12 18v4"/></svg><h3 class="display">Space.</h3><p>Big tables, good light, plenty of outlets, everything set up before anyone walks in. Bring the project. That's the whole packing list.</p></div>
<div class="card shadow-pink"><svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><circle cx="17" cy="9" r="2.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M14 19.5a4.5 4.5 0 0 1 7.5-2.5"/></svg><h3 class="display">People.</h3><p>A room full of people who came for the same reason. Nobody has to explain what they're working on or why it matters.</p></div>
</div>
<p class="btn-row"><a class="btn btn-accent" href="#book">Book a Weekend</a></p>
</div></section>
<section class="band band-marigold"><div class="wrap">
<h2 class="display">Four ways to get a weekend back.</h2>
<div class="grid grid-2">
<a class="card card-link shadow-ink" href="hobby-retreats.html"><h3 class="display text-rust">Hobby Retreats</h3><p>Quilting, sewing, scrapbooking, and craft weekends. Big tables, good light, and forty-eight hours with the project.</p><span class="more">Learn more</span></a>
<a class="card card-link shadow-ink" href="gaming-getaways.html"><h3 class="display text-plum">Gaming Getaways</h3><p>Tabletop weekends for people whose campaign never gets past session three.</p><span class="more">Learn more</span></a>
<a class="card card-link shadow-ink" href="corporate-retreats.html"><h3 class="display text-blue">Corporate Retreats</h3><p>Offsites run like a production, by someone who has spent twenty years opening shows on time.</p><span class="more">Learn more</span></a>
<a class="card card-link shadow-ink" href="private-groups.html"><h3 class="display text-green">Private Groups</h3><p>Guilds, clubs, and friend groups bring the people. Nikki handles everything else.</p><span class="more">Learn more</span></a>
</div>
</div></section>
<section id="nikki" class="band band-peach"><div class="wrap guide">
<div class="guide-photo"><svg class="petals" viewBox="0 0 200 200" aria-hidden="true"><circle cx="166.0" cy="100.0" r="33" fill="#F6B93B"/><circle cx="146.7" cy="146.7" r="33" fill="#FF8FD8"/><circle cx="100.0" cy="166.0" r="33" fill="#6FC3FF"/><circle cx="53.3" cy="146.7" r="33" fill="#3ECF8E"/><circle cx="34.0" cy="100.0" r="33" fill="#FF6B6B"/><circle cx="53.3" cy="53.3" r="33" fill="#F6B93B"/><circle cx="100.0" cy="34.0" r="33" fill="#FF8FD8"/><circle cx="146.7" cy="53.3" r="33" fill="#3ECF8E"/></svg>{img("nikki-headshot", "Nikki, smiling, red curly hair, olive jacket", widths=[380, 760], sizes="(max-width: 900px) 230px, 270px", w=1024, h=1024)}<span class="badge">Nikki, Freckle Flower</span></div>
<div class="prose">
<h2 class="display">Twenty years of costumes, one very neglected garden.</h2>
<p>I'm Nikki. I spent twenty years as a costume designer for theatre and cosplay, which means I've spent most of my adult life in a workroom full of people building something together, up to our elbows in fabric, losing track of time. I know what that room does for a person. I also know what happens when life crowds it out. My own garden could tell you.</p>
<p>I'm also the planner in my family. Airbnbs for the trips, venues for the parties, the whole itinerary. Somewhere along the way I noticed that planning an event is a lot like planning a play. It's a full production. There are a hundred moving parts and deadlines that have to be met, even when they aren't. Opening night doesn't move. Theatre taught me how to get everything ready anyway.</p>
<p class="strong">So that's my job here. I run the production. You show up and do the thing you love.</p>
<div class="pills"><span>Twenty years in costume design</span><span>Theatre and cosplay</span><span>The family's trip planner</span></div>
</div>
</div></section>
<section class="band band-mint"><div class="wrap">
<h2 class="display">Three steps between you and a weekend off.</h2>
<div class="grid grid-3 steps">
<div class="step step-marigold"><div class="display num text-rust">1</div><h3>Pick your retreat.</h3><p>Choose the weekend that fits and a date that works.</p></div>
<div class="step step-mint"><div class="display num text-green">2</div><h3>Show up.</h3><p>The venue is booked, the room is set, and the snacks are out when you arrive. Bring the project and nothing else.</p></div>
<div class="step step-pink"><div class="display num text-plum">3</div><h3>Recharge.</h3><p>Two days with the project and the people. Then home, rested in a way a vacation never quite manages.</p></div>
</div>
<p class="btn-row"><a class="btn btn-accent" href="#book">Book a Weekend</a></p>
</div></section>
<section class="band"><div class="wrap two-col">
<h2 class="display">Weekend retreats in Arkansas</h2>
<div class="prose">
<p>Most people have something they love doing that they almost never get to do. It's a real part of who they are, and when it goes untouched for long enough, they feel it. The days start running together. Work and family take everything, and the fun, whimsical part of a person gets quiet. Muscles that don't get used stop working.</p>
<p>Freckle Flower Event Planning runs weekend retreats in Arkansas, built on one idea: everyone deserves the chance to shamelessly pursue what they enjoy, alongside people who want the same thing. Every weekend comes with a proposal that spells out the venue, the setup, the snacks, and the catering. The space is ready before anyone arrives.</p>
<p class="strong">Nobody has to be an expert. Nobody has to bring a finished project. If you've got something you love and no time to do it, that's the whole qualification.</p>
<p><a class="link" href="faq.html">Read the FAQ</a></p>
</div>
</div></section>
<section class="band band-peach"><div class="wrap"><div class="card lead-card shadow-sky">
<div>
<h2 class="display">The retreat packing list, from someone who has packed for a hundred productions.</h2>
<p>A printable packing list for a weekend hobby retreat. What to bring, what to leave home, and the three things everyone forgets. Drop an email, get the PDF, and get first notice when a weekend opens up.</p>
</div>
<form class="form" action="https://formspree.io/f/REPLACE_ME" method="POST">
<label for="fn">First name</label><input id="fn" name="name" type="text" placeholder="First name" required>
<label for="em">Email</label><input id="em" name="email" type="email" placeholder="you@example.com" required>
<label for="hb">Which hobby?</label><select id="hb" name="hobby"><option>Quilting</option><option>Sewing</option><option>Scrapbooking</option><option>Tabletop gaming</option><option>Something else</option></select>
<button class="btn btn-ink" type="submit">Send Me the List</button>
</form>
</div></div></section>
""" + cta_band("The project is waiting. So are the people.", "Book a Weekend") + footer()
write("index.html", home)
