
import React, { useState } from 'react';
import { Mail, MapPin, Phone } from 'lucide-react';

const Contact = () => {
  const [formSubmitted, setFormSubmitted] = useState(false);
  
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // In a real application, you would handle form submission here
    setFormSubmitted(true);
    setTimeout(() => setFormSubmitted(false), 3000);
  };
  
  return (
    <section id="contact" className="section-container bg-secondary/50">
      <div className="text-center max-w-3xl mx-auto mb-16">
        <h2 className="heading-lg mb-4">Get In Touch</h2>
        <p className="subheading mx-auto">
          I'm always open to discussing new projects, opportunities, or partnerships.
          Feel free to reach out to me using the form below or through my contact details.
        </p>
      </div>
      
      <div className="grid md:grid-cols-2 gap-12 max-w-4xl mx-auto">
        <div>
          <div className="space-y-8">
            <div className="flex items-start gap-4">
              <div className="bg-primary/10 p-3 rounded-lg">
                <Mail className="text-primary h-6 w-6" />
              </div>
              <div>
                <h4 className="text-lg font-semibold mb-1">Email</h4>
                <a href="mailto:baralanupam111@gmail.com" className="text-muted-foreground hover:text-foreground transition-colors">
                  baralanupam111@gmail.com
                </a>
              </div>
            </div>
            
            <div className="flex items-start gap-4">
              <div className="bg-primary/10 p-3 rounded-lg">
                <MapPin className="text-primary h-6 w-6" />
              </div>
              <div>
                <h4 className="text-lg font-semibold mb-1">Location</h4>
                <p className="text-muted-foreground">
                  Sunwal, Nepal
                </p>
              </div>
            </div>
            
            <div className="flex items-start gap-4">
              <div className="bg-primary/10 p-3 rounded-lg">
                <Phone className="text-primary h-6 w-6" />
              </div>
              <div>
                <h4 className="text-lg font-semibold mb-1">Phone</h4>
                <a href="tel:+9779767606302" className="text-muted-foreground hover:text-foreground transition-colors">
                  +977 9767606302
                </a>
              </div>
            </div>
          </div>
        </div>
        
        <div>
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="grid grid-cols-2 gap-6">
              <div>
                <label htmlFor="name" className="block text-sm font-medium text-foreground mb-1">
                  Name
                </label>
                <input
                  type="text"
                  id="name"
                  placeholder="Your Name"
                  className="w-full px-4 py-3 bg-background border border-input rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  required
                />
              </div>
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-foreground mb-1">
                  Email
                </label>
                <input
                  type="email"
                  id="email"
                  placeholder="your.email@example.com"
                  className="w-full px-4 py-3 bg-background border border-input rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  required
                />
              </div>
            </div>
            
            <div>
              <label htmlFor="subject" className="block text-sm font-medium text-foreground mb-1">
                Subject
              </label>
              <input
                type="text"
                id="subject"
                placeholder="How can I help you?"
                className="w-full px-4 py-3 bg-background border border-input rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                required
              />
            </div>
            
            <div>
              <label htmlFor="message" className="block text-sm font-medium text-foreground mb-1">
                Message
              </label>
              <textarea
                id="message"
                rows={5}
                placeholder="Your message here..."
                className="w-full px-4 py-3 bg-background border border-input rounded-lg focus:outline-none focus:ring-2 focus:ring-primary resize-none"
                required
              ></textarea>
            </div>
            
            <button
              type="submit"
              className="btn-primary w-full"
            >
              {formSubmitted ? 'Message Sent!' : 'Send Message'}
            </button>
          </form>
        </div>
      </div>
    </section>
  );
};

export default Contact;
