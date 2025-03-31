
import React, { useEffect, useRef } from 'react';
import { ArrowDownCircle, Github, Linkedin, Mail } from 'lucide-react';

const Hero = () => {
  const codeRef = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    if (!codeRef.current) return;
    
    // This simulates typing code animation
    const codeLines = [
      'const developer = {',
      '  name: "Anupam Baral",',
      '  role: "Currently Learning",',
      '  skills: ["HTML5", "CSS", "JavaScript", "Python", "C", "Java"],',
      '  education: "Bachelor (2023-Running)",',
      '  campus: "Butwal Kalika Campus, Butwal"',
      '};',
      '',
      'function createPortfolio() {',
      '  return developer.skills.map(skill => {',
      '    return `Building with ${skill}`;',
      '  });',
      '}'
    ];
    
    let currentLine = 0;
    let currentChar = 0;
    let typingInterval: NodeJS.Timeout;
    
    const startTyping = () => {
      typingInterval = setInterval(() => {
        if (currentLine >= codeLines.length) {
          clearInterval(typingInterval);
          return;
        }
        
        const lineElement = document.getElementById(`code-line-${currentLine}`);
        if (!lineElement) return;
        
        const currentText = codeLines[currentLine].substring(0, currentChar + 1);
        lineElement.textContent = currentText;
        
        currentChar++;
        
        if (currentChar >= codeLines[currentLine].length) {
          currentLine++;
          currentChar = 0;
        }
      }, 30);
    };
    
    setTimeout(startTyping, 500);
    
    return () => clearInterval(typingInterval);
  }, []);

  return (
    <section id="home" className="min-h-screen pt-24 flex items-center">
      <div className="container-custom grid md:grid-cols-2 gap-12 items-center">
        <div className="order-2 md:order-1">
          <div className="opacity-0 animate-fade-in">
            <div className="inline-block bg-primary/10 text-primary px-3 py-1 rounded-full text-sm font-medium mb-4">
              Currently Learning
            </div>
          </div>
          
          <h1 className="heading-xl mb-4 opacity-0 animate-fade-in animate-delay-100 text-balance">
            Hello, I'm <span className="text-primary">Anupam Baral</span>
          </h1>
          
          <p className="subheading mb-8 opacity-0 animate-fade-in animate-delay-200 text-balance">
            I'm passionate about programming and currently pursuing my Bachelor's degree
            at Butwal Kalika Campus, Butwal, affiliated with Tribhuvan University.
          </p>
          
          <div className="flex flex-wrap gap-4 mb-8 opacity-0 animate-fade-in animate-delay-300">
            <a href="#projects" className="btn-primary">
              View Projects
            </a>
            <a href="#contact" className="btn-secondary">
              Contact Me
            </a>
          </div>
          
          <div className="flex gap-6 opacity-0 animate-fade-in animate-delay-400">
            <a href="https://github.com" target="_blank" rel="noopener noreferrer" 
              className="opacity-70 hover:opacity-100 transition-opacity">
              <Github size={20} />
            </a>
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer"
              className="opacity-70 hover:opacity-100 transition-opacity">
              <Linkedin size={20} />
            </a>
            <a href="mailto:contact@anupambaral.dev" 
              className="opacity-70 hover:opacity-100 transition-opacity">
              <Mail size={20} />
            </a>
          </div>
        </div>
        
        <div className="order-1 md:order-2 opacity-0 animate-fade-in animate-delay-200">
          <div ref={codeRef} className="bg-black/5 backdrop-blur-sm rounded-lg p-6 font-mono text-sm leading-relaxed overflow-hidden">
            {Array.from({ length: 11 }).map((_, index) => (
              <div key={index} id={`code-line-${index}`} className={index === 6 ? 'h-4' : ''}>
                &nbsp;
              </div>
            ))}
          </div>
        </div>
        
        <div className="absolute bottom-12 left-1/2 transform -translate-x-1/2 animate-float hidden md:block opacity-0 animate-fade-in animate-delay-500">
          <a href="#projects" aria-label="Scroll to projects section">
            <ArrowDownCircle className="text-primary/70" />
          </a>
        </div>
      </div>
    </section>
  );
};

export default Hero;
