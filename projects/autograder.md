---
layout: page
title: "AutoGrader"
---


In my final year of undergraduate studies, I was asked to develop a new test grading system for the applied mathematics department. Their current system required custom multiple-choice template paper, which was expensive. Furthermore, they wanted a solution that allowed students to fill in decimal-valued answers. To solve this issue, I studied up image processing, probabilistic graphical models and neural networks.

### Version 1 (2016-2017)

I wanted to create something that could actually be used by the university. My proposed solution can be found in this [report]( /assets/pdfs/Skripsie.pdf). The basic idea was to use a <a href="https://en.wikipedia.org/wiki/Radon_transform"  target="_blank">radon transform</a> to locate the template itself. Once the template has been located the system would use image processing to find the individual bubbles in the image. Lastly, the bubbles would be processed to determine whether they were filled in or not. The blocks ([see report]( /assets/pdfs/Skripsie.pdf)) were also processed using a CNN to determine what the digits were filled in. A final prediction was then made using a <a href="https://towardsdatascience.com/introduction-to-probabilistic-graphical-models-b8e0bf459812"  target="_blank">probabilistic graphical model (PGM)</a>.

### Version 2 (2018 - 2019)

The version discussed above worked, but required a lot of input from my side. The department would send me the tests, I would grade them and then send the results back to the department. I also had to manually check tests where the system was unsure. For the next version, I decided to build a website. This website allowed lecturers to upload their tests and then the system could automatically grade them. I still had to manually check any tests the system was unsure about.

### Version 3 (2020 - 2023)
The version 2 system was still not scalable. It was not accurate enough and I still had to do the manual corrections. To allow the entire university to use it, I decided to do a complete revamp of the system. I through out all the old code and started over. The new system uses standard position markers as used in <a href="https://blog.beaconstac.com/2022/07/comprehensive-guide-to-qr-code/"  target="_blank">QR codes</a>, which are more accurate. I simplified the template design to allow the system to only read raw text as filled in by the students. This made it easier for the students when writing tests, but this is a much more difficult task to solve with image processing. To address this issue, I switched to using a convolutional neural network as an encoder and a transformer as the decoder. Furthermore, I upgraded the system to continuously improve as more tests were submitted. The system now learns from any corrections made by the lecturers and I improved the website functionality to allow lecturers to inspect the tests themselves. Furthermore, the system was now accurate enough that the inspection phase was really fast.

In 2023 the system is now being rolled out to the entire Stellenbosch University. The AutoGrader website can be found <a href="https://autograde.ngrok.io"  target="_blank">here</a>.
