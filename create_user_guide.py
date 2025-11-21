from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white, blue, green, red
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
import os
from datetime import datetime

def create_user_guide():
    """Create a comprehensive PDF user guide"""
    
    # Create PDF document
    doc = SimpleDocTemplate(
        "AI_Outfit_Skin_Advisor_User_Guide.pdf",
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18
    )
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=HexColor('#667eea'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor=HexColor('#2C3E50'),
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=8,
        textColor=HexColor('#34495E'),
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    step_style = ParagraphStyle(
        'StepStyle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        leftIndent=20,
        fontName='Helvetica'
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        fontName='Courier',
        backColor=HexColor('#f8f9fa'),
        borderColor=HexColor('#dee2e6'),
        borderWidth=1,
        borderPadding=8
    )
    
    # Story content
    story = []
    
    # Title page
    story.append(Paragraph("AI-Based Outfit and Skin Advisor", title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Complete User Guide", styles['Heading2']))
    story.append(Spacer(1, 0.3*inch))
    
    # Introduction
    story.append(Paragraph("📱 Welcome to Your Personal AI Style Assistant", heading_style))
    story.append(Paragraph(
        "This comprehensive guide will walk you through using the AI-powered outfit and skincare "
        "recommendation system. The application uses advanced computer vision and machine learning "
        "to analyze your skin tone and type, then provides personalized fashion and beauty advice.",
        body_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Features overview
    story.append(Paragraph("🌟 Key Features", heading_style))
    features = [
        "• AI-powered skin tone detection (Light/Medium/Deep with Cool/Warm undertones)",
        "• Skin type classification (Dry, Oily, Normal, Combination)",
        "• ML-based outfit recommendations for different occasions",
        "• Personalized color palette suggestions",
        "• Skincare product recommendations",
        "• Interactive AI chatbot for beauty advice",
        "• E-commerce integration with shopping links",
        "• Real-time weather integration for seasonal recommendations"
    ]
    
    for feature in features:
        story.append(Paragraph(feature, step_style))
    
    story.append(PageBreak())
    
    # System Requirements
    story.append(Paragraph("💻 System Requirements & Setup", heading_style))
    story.append(Paragraph("Before starting, ensure you have:", subheading_style))
    
    requirements = [
        "• Python 3.8 or higher installed",
        "• All dependencies installed (Flask, OpenCV, scikit-learn, etc.)",
        "• Web browser (Chrome, Firefox, Safari, or Edge)",
        "• Internet connection for weather data",
        "• Camera or image files for skin analysis"
    ]
    
    for req in requirements:
        story.append(Paragraph(req, step_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Step-by-step instructions
    story.append(Paragraph("🚀 Step-by-Step Instructions", heading_style))
    
    # Step 1: Starting the Application
    story.append(Paragraph("Step 1: Starting the Application", subheading_style))
    story.append(Paragraph("1.1 Open your terminal or command prompt", step_style))
    story.append(Paragraph("1.2 Navigate to the project directory:", step_style))
    story.append(Paragraph("cd /workspace", code_style))
    story.append(Paragraph("1.3 Start the Flask application:", step_style))
    story.append(Paragraph("python app.py", code_style))
    story.append(Paragraph(
        "1.4 Wait for the server to start. You should see output similar to:",
        step_style
    ))
    story.append(Paragraph(
        "* Running on http://127.0.0.1:5000<br/>"
        "* Debug mode: on<br/>"
        "Starting AI Outfit and Skin Advisor...<br/>"
        "Outfit dataset: 48 records<br/>"
        "Skincare dataset: 40 records",
        code_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Step 2: Opening the Web Interface
    story.append(Paragraph("Step 2: Opening the Web Interface", subheading_style))
    story.append(Paragraph("2.1 Open your web browser", step_style))
    story.append(Paragraph("2.2 Navigate to the application URL:", step_style))
    story.append(Paragraph("http://localhost:5000", code_style))
    story.append(Paragraph(
        "2.3 You should see the AI Style Advisor homepage with:",
        step_style
    ))
    story.append(Paragraph(
        "• Animated gradient background with floating shapes<br/>"
        "• Professional navigation header<br/>"
        "• Hero section with feature highlights<br/>"
        "• Main analysis form on the right side",
        step_style
    ))
    
    story.append(PageBreak())
    
    # Step 3: Using the Analysis Form
    story.append(Paragraph("Step 3: Performing Skin and Style Analysis", subheading_style))
    
    story.append(Paragraph("3.1 Fill in Personal Information", body_style))
    story.append(Paragraph("• Select your Gender: Male, Female, or Other", step_style))
    story.append(Paragraph("• Choose the Occasion: Party, College, Office, Marriage, Casual, Formal, Date, or Travel", step_style))
    story.append(Paragraph("• Enter your City: This helps determine weather and seasonal recommendations", step_style))
    
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("3.2 Upload Your Photo", body_style))
    story.append(Paragraph("• Click the 'Upload Your Photo' area", step_style))
    story.append(Paragraph("• Select a clear, well-lit photo of your face", step_style))
    story.append(Paragraph("• Supported formats: JPG, PNG (maximum 16MB)", step_style))
    story.append(Paragraph("• For testing, you can use the provided test images:", step_style))
    story.append(Paragraph(
        "  - /images/SkinTone.jpg (Light warm skin tone)<br/>"
        "  - /images/SkinTone.jpg (Medium warm skin tone)<br/>"
        "  - /images/SkinToneAnalysis.jpg (Deep warm skin tone)",
        step_style
    ))
    
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("3.3 Start Analysis", body_style))
    story.append(Paragraph("• Click the 'Analyze My Style' button", step_style))
    story.append(Paragraph("• Wait for the AI processing (usually 5-10 seconds)", step_style))
    story.append(Paragraph("• You'll see a loading animation with 'Analyzing your photo with AI magic...'", step_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Step 4: Understanding Results
    story.append(Paragraph("Step 4: Understanding Your Results", subheading_style))
    
    story.append(Paragraph("4.1 Your Profile Summary", body_style))
    story.append(Paragraph("The results page displays your uploaded photo alongside:", step_style))
    story.append(Paragraph("• Your selected gender and occasion", step_style))
    story.append(Paragraph("• Current season and weather data", step_style))
    story.append(Paragraph("• Your city and temperature", step_style))
    
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("4.2 AI Skin Analysis", body_style))
    story.append(Paragraph("The AI provides detailed skin analysis:", step_style))
    story.append(Paragraph("• <b>Detected Skin Tone:</b> Light/Medium/Deep + Cool/Warm undertones", step_style))
    story.append(Paragraph("• <b>Detected Skin Type:</b> Dry, Oily, Normal, or Combination", step_style))
    story.append(Paragraph("• <b>Analysis Process:</b> Step-by-step breakdown of AI processing", step_style))
    
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("4.3 AI-Recommended Outfit", body_style))
    story.append(Paragraph("Personalized outfit suggestions include:", step_style))
    story.append(Paragraph("• Specific outfit name tailored to your inputs", step_style))
    story.append(Paragraph("• Color palette with 4 complementary colors for your skin tone", step_style))
    story.append(Paragraph("• Shopping links to Amazon, Flipkart, and Meesho", step_style))
    story.append(Paragraph("• Prediction method badge (ML Model/Dataset Search/Fallback)", step_style))
    
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("4.4 Personalized Skincare Recommendations", body_style))
    story.append(Paragraph("Based on your detected skin type:", step_style))
    story.append(Paragraph("• Curated product recommendations with images", step_style))
    story.append(Paragraph("• Product descriptions and brand information", step_style))
    story.append(Paragraph("• Direct links to purchase products", step_style))
    story.append(Paragraph("• Custom skincare tips for your skin type", step_style))
    
    story.append(PageBreak())
    
    # Step 5: Using the AI Chatbot
    story.append(Paragraph("Step 5: Interacting with the AI Chatbot", subheading_style))
    
    story.append(Paragraph("5.1 Accessing the Chatbot", body_style))
    story.append(Paragraph("• Look for the floating chat icon in the bottom-right corner", step_style))
    story.append(Paragraph("• Click the circular icon with the chat symbol", step_style))
    story.append(Paragraph("• The chatbot window will expand", step_style))
    
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("5.2 Chatbot Capabilities", body_style))
    story.append(Paragraph("The AI assistant can help with:", step_style))
    story.append(Paragraph("• Skincare routines and product advice", step_style))
    story.append(Paragraph("• Outfit coordination and color matching", step_style))
    story.append(Paragraph("• Beauty tips and glow enhancement", step_style))
    story.append(Paragraph("• Personalized advice based on your detected skin type", step_style))
    
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("5.3 Sample Questions to Ask", body_style))
    sample_questions = [
        "• 'What skincare routine is best for my oily skin?'",
        "• 'What colors look good on warm skin tones?'",
        "• 'Give me outfit tips for a party'",
        "• 'How can I make my skin glow naturally?'",
        "• 'What makeup colors suit my skin tone?'"
    ]
    
    for question in sample_questions:
        story.append(Paragraph(question, step_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Step 6: Additional Features
    story.append(Paragraph("Step 6: Additional Features", subheading_style))
    
    story.append(Paragraph("6.1 Saving and Sharing Results", body_style))
    story.append(Paragraph("• Click 'Save Results' to print or save as PDF", step_style))
    story.append(Paragraph("• Click 'Share Analysis' to share your results", step_style))
    story.append(Paragraph("• Click 'New Analysis' to start over with a different photo", step_style))
    
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("6.2 Shopping Integration", body_style))
    story.append(Paragraph("• Click shopping buttons to browse similar outfits", step_style))
    story.append(Paragraph("• Links open in new tabs to preserve your analysis", step_style))
    story.append(Paragraph("• Available platforms: Amazon, Flipkart, Meesho", step_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Troubleshooting
    story.append(Paragraph("🔧 Troubleshooting Common Issues", heading_style))
    
    troubleshooting_items = [
        {
            "issue": "Application won't start",
            "solution": "Ensure all dependencies are installed with: pip install -r requirements.txt"
        },
        {
            "issue": "Image upload fails",
            "solution": "Check file size (max 16MB) and format (JPG/PNG only)"
        },
        {
            "issue": "No skin tone detected",
            "solution": "Use a clear, well-lit photo with visible face. Avoid heavy makeup or filters"
        },
        {
            "issue": "Weather data not loading",
            "solution": "Check internet connection. The app uses fallback data if API fails"
        },
        {
            "issue": "Chatbot not responding",
            "solution": "Refresh the page and try again. Check browser console for errors"
        }
    ]
    
    for item in troubleshooting_items:
        story.append(Paragraph(f"<b>Issue:</b> {item['issue']}", body_style))
        story.append(Paragraph(f"<b>Solution:</b> {item['solution']}", step_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # Technical Details
    story.append(Paragraph("⚙️ Technical Details", heading_style))
    
    story.append(Paragraph("AI Technologies Used", subheading_style))
    tech_details = [
        "• <b>Computer Vision:</b> OpenCV for image processing and skin analysis",
        "• <b>Machine Learning:</b> RandomForest classifier for outfit predictions",
        "• <b>Color Analysis:</b> HSV color space for accurate skin tone detection",
        "• <b>Texture Analysis:</b> Local Binary Patterns for skin type classification",
        "• <b>Weather Integration:</b> OpenWeatherMap API for real-time data",
        "• <b>Frontend:</b> Modern HTML5, CSS3, JavaScript with animations",
        "• <b>Backend:</b> Flask web framework with RESTful APIs"
    ]
    
    for detail in tech_details:
        story.append(Paragraph(detail, step_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Dataset Information
    story.append(Paragraph("Dataset Information", subheading_style))
    story.append(Paragraph("• <b>Outfit Dataset:</b> 48 carefully curated outfit combinations", step_style))
    story.append(Paragraph("• <b>Skincare Dataset:</b> 40+ products across all skin types", step_style))
    story.append(Paragraph("• <b>Categories:</b> Multiple genders, occasions, seasons, and skin tones", step_style))
    story.append(Paragraph("• <b>E-commerce Links:</b> Direct integration with major shopping platforms", step_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Footer
    story.append(Paragraph("📞 Support & Contact", heading_style))
    story.append(Paragraph(
        "For technical support or questions about the AI Outfit and Skin Advisor, "
        "please refer to the README.md file in the project directory or contact the development team.",
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(f"Generated on: {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
    story.append(Paragraph("Version: 1.0", styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print("✅ User guide PDF created successfully: AI_Outfit_Skin_Advisor_User_Guide.pdf")

if __name__ == "__main__":
    create_user_guide()