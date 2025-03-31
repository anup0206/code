
import React, { useState, useEffect } from 'react';
import { cn } from '@/lib/utils';

const Header = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 10);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header
      className={cn(
        'fixed top-0 left-0 right-0 z-50 py-4 transition-all duration-300',
        isScrolled ? 'bg-white/80 backdrop-blur-lg shadow-sm' : 'bg-transparent'
      )}
    >
      <div className="container-custom flex items-center justify-between">
        <a 
          href="#home" 
          className="text-xl font-display font-bold"
        >
          Anupam.dev
        </a>

        {/* Desktop Menu */}
        <nav className="hidden md:flex items-center space-x-8">
          {['home', 'projects', 'skills', 'about', 'contact'].map((item) => (
            <a
              key={item}
              href={`#${item}`}
              className="font-medium opacity-80 hover:opacity-100 transition-opacity link-underline"
            >
              {item.charAt(0).toUpperCase() + item.slice(1)}
            </a>
          ))}
        </nav>

        {/* Mobile Menu Toggle */}
        <button 
          className="md:hidden flex flex-col space-y-1.5 p-2" 
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          aria-label="Toggle menu"
        >
          <span className={cn(
            "block w-6 h-0.5 bg-foreground transition-transform duration-300",
            mobileMenuOpen && "translate-y-2 rotate-45"
          )}></span>
          <span className={cn(
            "block w-6 h-0.5 bg-foreground transition-opacity duration-300",
            mobileMenuOpen && "opacity-0"
          )}></span>
          <span className={cn(
            "block w-6 h-0.5 bg-foreground transition-transform duration-300",
            mobileMenuOpen && "-translate-y-2 -rotate-45"
          )}></span>
        </button>

        {/* Mobile Menu */}
        <div className={cn(
          "absolute top-full left-0 right-0 bg-white/95 backdrop-blur-lg shadow-lg py-4 transition-all duration-300 flex flex-col",
          mobileMenuOpen ? "opacity-100 translate-y-0" : "opacity-0 -translate-y-4 pointer-events-none"
        )}>
          {['home', 'projects', 'skills', 'about', 'contact'].map((item) => (
            <a
              key={item}
              href={`#${item}`}
              className="py-3 px-8 font-medium hover:bg-secondary transition-colors"
              onClick={() => setMobileMenuOpen(false)}
            >
              {item.charAt(0).toUpperCase() + item.slice(1)}
            </a>
          ))}
        </div>
      </div>
    </header>
  );
};

export default Header;
