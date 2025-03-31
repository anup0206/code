
import React from 'react';
import { Heart } from 'lucide-react';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="py-12 bg-foreground text-primary-foreground">
      <div className="container-custom">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="mb-6 md:mb-0">
            <div className="text-2xl font-display font-bold mb-2">Anupam.dev</div>
            <p className="text-primary-foreground/70 text-sm">
              Building exceptional digital experiences
            </p>
          </div>
          
          <div className="flex flex-col items-center md:items-end">
            <div className="flex gap-8 mb-4">
              {['Home', 'Projects', 'Skills', 'About', 'Contact'].map((item) => (
                <a 
                  key={item} 
                  href={`#${item.toLowerCase()}`}
                  className="text-sm text-primary-foreground/70 hover:text-primary-foreground transition-colors"
                >
                  {item}
                </a>
              ))}
            </div>
            
            <div className="text-sm text-primary-foreground/50 flex items-center gap-1">
              <span>&copy; {currentYear} Anupam Baral. All rights reserved.</span>
              <span className="inline-flex items-center">
                Made with <Heart className="h-3 w-3 mx-1 text-red-400" /> and React
              </span>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
