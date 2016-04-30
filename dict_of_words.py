#!/usr/bin/python
import re


class WordCounter(object):

    def __init__(self, file_path):
        self.__word_counts = {}
        self.__reg_exp_list = []
        self.__mail = open(file_path)
        self.__create_reg_exps()
        self.__count_all_expressions()
        self.__count_capital_leters()

    def __count_word(self, reg_exp):
        words = re.findall(reg_exp, self.__mail.read().lower())
        self.__word_counts[reg_exp] = len(words)

    def __count_all_expressions(self):
        for expression in self.__reg_exp_list:
            self.__count_word(expression)

    def __count_capital_leters(self):
        self.__word_counts["CapitalLetters"] = sum(1 for c in self.__mail.read() if c.isupper())

    def __avg_capital_seq(self):
        pattern = '[A-Z]'
        str = self.__mail.read()
        m = re.findall(pattern, str)
        wynik = len(m)
        self.__word_counts["AvGCapitalSeq"] = wynik

    def __max_capital_seq(self):
        pattern = '[A-Z]+'
        str = self.__mail.read()
        m = re.findall(pattern, str)
        mlicz = []
        for i in m:
            mlicz.append(len(i))
        wynik = max(mlicz)
        self.__word_counts["MaxCapitalSeq"] = wynik

    def __create_reg_exps(self):
        self.__reg_exp_list.append(re.compile('data', re.I))
        self.__reg_exp_list.append(re.compile('\d\d\d', re.I))
        self.__reg_exp_list.append(re.compile('technolog', re.I))
        self.__reg_exp_list.append(re.compile('technique', re.I))
        self.__reg_exp_list.append(re.compile('technic', re.I))
        self.__reg_exp_list.append(re.compile('[1-2]\d\d\d', re.I))
        self.__reg_exp_list.append(re.compile('part', re.I))
        self.__reg_exp_list.append(re.compile('[a,p]m', re.I))
        self.__reg_exp_list.append(re.compile('cs', re.I))
        self.__reg_exp_list.append(re.compile('direct', re.I))
        self.__reg_exp_list.append(re.compile('meeting', re.I))
        self.__reg_exp_list.append(re.compile('or[i,y]ginal', re.I))
        self.__reg_exp_list.append(re.compile('project', re.I))
        self.__reg_exp_list.append(re.compile('re', re.I))
        self.__reg_exp_list.append(re.compile('edu', re.I))
        self.__reg_exp_list.append(re.compile('table', re.I))
        self.__reg_exp_list.append(re.compile('conference', re.I))
        self.__reg_exp_list.append(re.compile('sale', re.I))
        self.__reg_exp_list.append(re.compile('award', re.I))
        self.__reg_exp_list.append(re.compile('winner', re.I))
        self.__reg_exp_list.append(re.compile('lucky', re.I))
        self.__reg_exp_list.append(re.compile('$', re.I))
        self.__reg_exp_list.append(re.compile('#', re.I))
        self.__reg_exp_list.append(re.compile('make', re.I))
        self.__reg_exp_list.append(re.compile('address', re.I))
        self.__reg_exp_list.append(re.compile('all', re.I))
        self.__reg_exp_list.append(re.compile('\d\d', re.I))
        self.__reg_exp_list.append(re.compile('our', re.I))
        self.__reg_exp_list.append(re.compile('over', re.I))
        self.__reg_exp_list.append(re.compile('remove', re.I))
        self.__reg_exp_list.append(re.compile('intenet', re.I))
        self.__reg_exp_list.append(re.compile('order', re.I))
        self.__reg_exp_list.append(re.compile('mail', re.I))
        self.__reg_exp_list.append(re.compile('receive', re.I))
        self.__reg_exp_list.append(re.compile('will', re.I))
        self.__reg_exp_list.append(re.compile('people', re.I))
        self.__reg_exp_list.append(re.compile('report', re.I))
        self.__reg_exp_list.append(re.compile('addres', re.I))
        self.__reg_exp_list.append(re.compile('free', re.I))
        self.__reg_exp_list.append(re.compile(';', re.I))
        self.__reg_exp_list.append(re.compile('\(', re.I))
        self.__reg_exp_list.append(re.compile('business', re.I))
        self.__reg_exp_list.append(re.compile('email', re.I))
        self.__reg_exp_list.append(re.compile('you', re.I))
        self.__reg_exp_list.append(re.compile('credit', re.I))
        self.__reg_exp_list.append(re.compile('your', re.I))
        self.__reg_exp_list.append(re.compile('font', re.I))
        self.__reg_exp_list.append(re.compile('money', re.I))
        self.__reg_exp_list.append(re.compile('hp', re.I))
        self.__reg_exp_list.append(re.compile('hpl', re.I))
        self.__reg_exp_list.append(re.compile('george', re.I))
        self.__reg_exp_list.append(re.compile('lab', re.I))
        self.__reg_exp_list.append(re.compile('labs', re.I))
        self.__reg_exp_list.append(re.compile('telnet', re.I))
        self.__reg_exp_list.append(re.compile('\[', re.I))
        self.__reg_exp_list.append(re.compile('!', re.I))
        self.__reg_exp_list.append(re.compile('Addresses on CD', re.I))
        self.__reg_exp_list.append(re.compile('Brand new pager', re.I))
        self.__reg_exp_list.append(re.compile('Celebrity', re.I))
        self.__reg_exp_list.append(re.compile('Legal', re.I))
        self.__reg_exp_list.append(re.compile('Phone', re.I))
        self.__reg_exp_list.append(re.compile('Beverage', re.I))
        self.__reg_exp_list.append(re.compile('Cable converter', re.I))
        self.__reg_exp_list.append(re.compile('Copy DVDs', re.I))
        self.__reg_exp_list.append(re.compile('Luxury car', re.I))
        self.__reg_exp_list.append(re.compile('Rolex', re.I))
        self.__reg_exp_list.append(re.compile('Bonus', re.I))
        self.__reg_exp_list.append(re.compile('Casino', re.I))
        self.__reg_exp_list.append(re.compile('Laser printer', re.I))
        self.__reg_exp_list.append(re.compile('New domain extensions', re.I))
        self.__reg_exp_list.append(re.compile('Stainless steel', re.I))
        self.__reg_exp_list.append(re.compile('Access', re.I))
        self.__reg_exp_list.append(re.compile('Apply Online', re.I))
        self.__reg_exp_list.append(re.compile('Can\'t live without it', re.I))
        self.__reg_exp_list.append(re.compile('Don\'t hesitate', re.I))
        self.__reg_exp_list.append(re.compile('For you', re.I))
        self.__reg_exp_list.append(re.compile('Great offer', re.I))
        self.__reg_exp_list.append(re.compile('Instant', re.I))
        self.__reg_exp_list.append(re.compile('Now', re.I))
        self.__reg_exp_list.append(re.compile('Once in lifetime', re.I))
        self.__reg_exp_list.append(re.compile('Order now', re.I))
        self.__reg_exp_list.append(re.compile('Special promotion', re.I))
        self.__reg_exp_list.append(re.compile('Time limited', re.I))
        self.__reg_exp_list.append(re.compile('Act Now!', re.I))
        self.__reg_exp_list.append(re.compile('Call free', re.I))
        self.__reg_exp_list.append(re.compile('Do it today', re.I))
        self.__reg_exp_list.append(re.compile('For instant access', re.I))
        self.__reg_exp_list.append(re.compile('Get it now', re.I))
        self.__reg_exp_list.append(re.compile('Info you requested', re.I))
        self.__reg_exp_list.append(re.compile('Limited time', re.I))
        self.__reg_exp_list.append(re.compile('Now only', re.I))
        self.__reg_exp_list.append(re.compile('One time', re.I))
        self.__reg_exp_list.append(re.compile('Order today', re.I))
        self.__reg_exp_list.append(re.compile('Supplies are limited', re.I))
        self.__reg_exp_list.append(re.compile('Urgent', re.I))
        self.__reg_exp_list.append(re.compile('Apply now', re.I))
        self.__reg_exp_list.append(re.compile('Call now', re.I))
        self.__reg_exp_list.append(re.compile('Don\'t delete', re.I))
        self.__reg_exp_list.append(re.compile('Get started now', re.I))
        self.__reg_exp_list.append(re.compile('Information you requested', re.I))
        self.__reg_exp_list.append(re.compile('New customers only', re.I))
        self.__reg_exp_list.append(re.compile('Offer expires', re.I))
        self.__reg_exp_list.append(re.compile('Only', re.I))
        self.__reg_exp_list.append(re.compile('Please read', re.I))
        self.__reg_exp_list.append(re.compile('Take action now', re.I))
        self.__reg_exp_list.append(re.compile('While supplies last', re.I))
        self.__reg_exp_list.append(re.compile('All natural', re.I))
        self.__reg_exp_list.append(re.compile('Certified', re.I))
        self.__reg_exp_list.append(re.compile('Fantastic deal', re.I))
        self.__reg_exp_list.append(re.compile('It\'s effective', re.I))
        self.__reg_exp_list.append(re.compile('Real thing', re.I))
        self.__reg_exp_list.append(re.compile('All new', re.I))
        self.__reg_exp_list.append(re.compile('Congratulations', re.I))
        self.__reg_exp_list.append(re.compile('For free', re.I))
        self.__reg_exp_list.append(re.compile('Outstanding values', re.I))
        self.__reg_exp_list.append(re.compile('Risk free', re.I))
        self.__reg_exp_list.append(re.compile('Amazing', re.I))
        self.__reg_exp_list.append(re.compile('Drastically reduced', re.I))
        self.__reg_exp_list.append(re.compile('Guaranteed', re.I))
        self.__reg_exp_list.append(re.compile('Promise you', re.I))
        self.__reg_exp_list.append(re.compile('Satisfaction guaranteed', re.I))
        self.__reg_exp_list.append(re.compile('Free consultation', re.I))
        self.__reg_exp_list.append(re.compile('Free grant money', re.I))
        self.__reg_exp_list.append(re.compile('Free DVDs', re.I))
        self.__reg_exp_list.append(re.compile('Free Instant', re.I))
        self.__reg_exp_list.append(re.compile('Free membership', re.I))
        self.__reg_exp_list.append(re.compile('Free preview', re.I))
        self.__reg_exp_list.append(re.compile('Free sample', re.I))
        self.__reg_exp_list.append(re.compile('Free access', re.I))
        self.__reg_exp_list.append(re.compile('Free hosting', re.I))
        self.__reg_exp_list.append(re.compile('Free investment', re.I))
        self.__reg_exp_list.append(re.compile('Free priority mail', re.I))
        self.__reg_exp_list.append(re.compile('Free trial', re.I))
        self.__reg_exp_list.append(re.compile('Free cell phone', re.I))
        self.__reg_exp_list.append(re.compile('Free gift', re.I))
        self.__reg_exp_list.append(re.compile('Free installation', re.I))
        self.__reg_exp_list.append(re.compile('Free leads', re.I))
        self.__reg_exp_list.append(re.compile('Free offer', re.I))
        self.__reg_exp_list.append(re.compile('Free quote', re.I))
        self.__reg_exp_list.append(re.compile('Free website', re.I))
        self.__reg_exp_list.append(re.compile('Cancel at any time', re.I))
        self.__reg_exp_list.append(re.compile('Get', re.I))
        self.__reg_exp_list.append(re.compile('Print out and fax', re.I))
        self.__reg_exp_list.append(re.compile('Compare', re.I))
        self.__reg_exp_list.append(re.compile('Give it away', re.I))
        self.__reg_exp_list.append(re.compile('See for yourself', re.I))
        self.__reg_exp_list.append(re.compile('Copy accurately', re.I))
        self.__reg_exp_list.append(re.compile('Print from signature', re.I))
        self.__reg_exp_list.append(re.compile('Sign up free today', re.I))
        self.__reg_exp_list.append(re.compile('Sign up for free today', re.I))
        self.__reg_exp_list.append(re.compile('Being a member', re.I))
        self.__reg_exp_list.append(re.compile('Cannot be combined with any other offer', re.I))
        self.__reg_exp_list.append(re.compile('Financial freedom', re.I))
        self.__reg_exp_list.append(re.compile('Guarantee', re.I))
        self.__reg_exp_list.append(re.compile('Important information regarding', re.I))
        self.__reg_exp_list.append(re.compile('Mail in order from', re.I))
        self.__reg_exp_list.append(re.compile('Nigerian', re.I))
        self.__reg_exp_list.append(re.compile('No claim form', re.I))
        self.__reg_exp_list.append(re.compile('No gimmick', re.I))
        self.__reg_exp_list.append(re.compile('No obligation', re.I))
        self.__reg_exp_list.append(re.compile('No selling', re.I))
        self.__reg_exp_list.append(re.compile('Not intended', re.I))
        self.__reg_exp_list.append(re.compile('Offer', re.I))
        self.__reg_exp_list.append(re.compile('Priority mail', re.I))
        self.__reg_exp_list.append(re.compile('Produced and send out', re.I))
        self.__reg_exp_list.append(re.compile('Stuff on sale', re.I))
        self.__reg_exp_list.append(re.compile('They\'re just giving away', re.I))
        self.__reg_exp_list.append(re.compile('Unsolicited', re.I))
        self.__reg_exp_list.append(re.compile('Warranty', re.I))
        self.__reg_exp_list.append(re.compile('What are you waiting for', re.I))
        self.__reg_exp_list.append(re.compile('Winner', re.I))
        self.__reg_exp_list.append(re.compile('You are a winner!', re.I))
        self.__reg_exp_list.append(re.compile('Billing address', re.I))
        self.__reg_exp_list.append(re.compile('Confidentially on all orders', re.I))
        self.__reg_exp_list.append(re.compile('Gift certificate', re.I))
        self.__reg_exp_list.append(re.compile('Have you been turned down', re.I))
        self.__reg_exp_list.append(re.compile('In accordance with law', re.I))
        self.__reg_exp_list.append(re.compile('Message contains', re.I))
        self.__reg_exp_list.append(re.compile('No age restriction', re.I))
        self.__reg_exp_list.append(re.compile('No disappointment', re.I))
        self.__reg_exp_list.append(re.compile('No inventory', re.I))
        self.__reg_exp_list.append(re.compile('No purchase necessary', re.I))
        self.__reg_exp_list.append(re.compile('No strings attached', re.I))
        self.__reg_exp_list.append(re.compile('Obligation', re.I))
        self.__reg_exp_list.append(re.compile('Per day', re.I))
        self.__reg_exp_list.append(re.compile('Pri[cz]e', re.I))
        self.__reg_exp_list.append(re.compile('Reserves the right', re.I))
        self.__reg_exp_list.append(re.compile('Terms and conditions', re.I))
        self.__reg_exp_list.append(re.compile('Trial', re.I))
        self.__reg_exp_list.append(re.compile('Vacation', re.I))
        self.__reg_exp_list.append(re.compile('We honor all', re.I))
        self.__reg_exp_list.append(re.compile('Who really wins', re.I))
        self.__reg_exp_list.append(re.compile('Winning', re.I))
        self.__reg_exp_list.append(re.compile('You have been selected', re.I))
        self.__reg_exp_list.append(re.compile('Call', re.I))
        self.__reg_exp_list.append(re.compile('Deal', re.I))
        self.__reg_exp_list.append(re.compile('Giving away', re.I))
        self.__reg_exp_list.append(re.compile('If only that were that easy', re.I))
        self.__reg_exp_list.append(re.compile('Long distance phone offer', re.I))
        self.__reg_exp_list.append(re.compile('Name brand', re.I))
        self.__reg_exp_list.append(re.compile('No catch', re.I))
        self.__reg_exp_list.append(re.compile('No experience', re.I))
        self.__reg_exp_list.append(re.compile('No middleman', re.I))
        self.__reg_exp_list.append(re.compile('No question asked', re.I))
        self.__reg_exp_list.append(re.compile('No[\s\-]obligation', re.I))
        self.__reg_exp_list.append(re.compile('Off shore', re.I))
        self.__reg_exp_list.append(re.compile('Per week', re.I))
        self.__reg_exp_list.append(re.compile('Prizes', re.I))
        self.__reg_exp_list.append(re.compile('Shopping spree', re.I))
        self.__reg_exp_list.append(re.compile('The best rates', re.I))
        self.__reg_exp_list.append(re.compile('Unlimited', re.I))
        self.__reg_exp_list.append(re.compile('Vacation offers', re.I))
        self.__reg_exp_list.append(re.compile('Weekend getaway', re.I))
        self.__reg_exp_list.append(re.compile('Win', re.I))
        self.__reg_exp_list.append(re.compile('Won', re.I))
        self.__reg_exp_list.append(re.compile('You are a winner', re.I))
        self.__reg_exp_list.append(re.compile('Avoid bankruptcy', re.I))
        self.__reg_exp_list.append(re.compile('Calling creditors', re.I))
        self.__reg_exp_list.append(re.compile('Consolidate debt and credit', re.I))
        self.__reg_exp_list.append(re.compile('Eliminate bad credit', re.I))
        self.__reg_exp_list.append(re.compile('Eliminate debt', re.I))
        self.__reg_exp_list.append(re.compile('Financially independent', re.I))
        self.__reg_exp_list.append(re.compile('Get out of debt', re.I))
        self.__reg_exp_list.append(re.compile('Get paid', re.I))
        self.__reg_exp_list.append(re.compile('Lower interest rate', re.I))
        self.__reg_exp_list.append(re.compile('Lower monthly payment', re.I))
        self.__reg_exp_list.append(re.compile('Lower your mortgage rate ', re.I))
        self.__reg_exp_list.append(re.compile('Lowest insurance rates', re.I))
        self.__reg_exp_list.append(re.compile('Pre-approved', re.I))
        self.__reg_exp_list.append(re.compile('Refinance home', re.I))
        self.__reg_exp_list.append(re.compile('Social security number', re.I))
        self.__reg_exp_list.append(re.compile('Your income', re.I))
        self.__reg_exp_list.append(re.compile('Acceptance', re.I))
        self.__reg_exp_list.append(re.compile('Accordingly', re.I))
        self.__reg_exp_list.append(re.compile('Avoid', re.I))
        self.__reg_exp_list.append(re.compile('Chance', re.I))
        self.__reg_exp_list.append(re.compile('Dormant', re.I))
        self.__reg_exp_list.append(re.compile('Freedom', re.I))
        self.__reg_exp_list.append(re.compile('Here', re.I))
        self.__reg_exp_list.append(re.compile('Hidden', re.I))
        self.__reg_exp_list.append(re.compile('Home', re.I))
        self.__reg_exp_list.append(re.compile('Leave', re.I))
        self.__reg_exp_list.append(re.compile('Lifetime', re.I))
        self.__reg_exp_list.append(re.compile('Lose', re.I))
        self.__reg_exp_list.append(re.compile('Medium', re.I))
        self.__reg_exp_list.append(re.compile('Maintained', re.I))
        self.__reg_exp_list.append(re.compile('Miracle', re.I))
        self.__reg_exp_list.append(re.compile('Never', re.I))
        self.__reg_exp_list.append(re.compile('Passwords', re.I))
        self.__reg_exp_list.append(re.compile('Problem', re.I))
        self.__reg_exp_list.append(re.compile('Remove', re.I))
        self.__reg_exp_list.append(re.compile('Reverses', re.I))
        self.__reg_exp_list.append(re.compile('Sample', re.I))
        self.__reg_exp_list.append(re.compile('Satisfaction', re.I))
        self.__reg_exp_list.append(re.compile('Solution', re.I))
        self.__reg_exp_list.append(re.compile('Stop', re.I))
        self.__reg_exp_list.append(re.compile('Success', re.I))
        self.__reg_exp_list.append(re.compile('Teen', re.I))
        self.__reg_exp_list.append(re.compile('Wife', re.I))
        self.__reg_exp_list.append(re.compile('Dear Friend', re.I))
        self.__reg_exp_list.append(re.compile('Friend', re.I))
        self.__reg_exp_list.append(re.compile('Hello', re.I))
        self.__reg_exp_list.append(re.compile('Ad', re.I))
        self.__reg_exp_list.append(re.compile('Auto email removal', re.I))
        self.__reg_exp_list.append(re.compile('Bulk email', re.I))
        self.__reg_exp_list.append(re.compile('Click', re.I))
        self.__reg_exp_list.append(re.compile('Click below', re.I))
        self.__reg_exp_list.append(re.compile('Click here', re.I))
        self.__reg_exp_list.append(re.compile('Click to remove', re.I))
        self.__reg_exp_list.append(re.compile('Direct email', re.I))
        self.__reg_exp_list.append(re.compile('Direct marketing', re.I))
        self.__reg_exp_list.append(re.compile('Email harvest', re.I))
        self.__reg_exp_list.append(re.compile('Email marketing', re.I))
        self.__reg_exp_list.append(re.compile('Form', re.I))
        self.__reg_exp_list.append(re.compile('Increase sales', re.I))
        self.__reg_exp_list.append(re.compile('Increase traffic', re.I))
        self.__reg_exp_list.append(re.compile('Increase your sales', re.I))
        self.__reg_exp_list.append(re.compile('Internet market', re.I))
        self.__reg_exp_list.append(re.compile('Internet marketing', re.I))
        self.__reg_exp_list.append(re.compile('Marketing', re.I))
        self.__reg_exp_list.append(re.compile('Marketing solutions', re.I))
        self.__reg_exp_list.append(re.compile('Mass email', re.I))
        self.__reg_exp_list.append(re.compile('Member', re.I))
        self.__reg_exp_list.append(re.compile('Month trial offer', re.I))
        self.__reg_exp_list.append(re.compile('More Internet Traffic', re.I))
        self.__reg_exp_list.append(re.compile('Multi level marketing', re.I))
        self.__reg_exp_list.append(re.compile('Notspam', re.I))
        self.__reg_exp_list.append(re.compile('One time mailing', re.I))
        self.__reg_exp_list.append(re.compile('Online marketing', re.I))
        self.__reg_exp_list.append(re.compile('Open', re.I))
        self.__reg_exp_list.append(re.compile('Opt in', re.I))
        self.__reg_exp_list.append(re.compile('Performance', re.I))
        self.__reg_exp_list.append(re.compile('Removal instructions', re.I))
        self.__reg_exp_list.append(re.compile('Sale', re.I))
        self.__reg_exp_list.append(re.compile('Sales', re.I))
        self.__reg_exp_list.append(re.compile('Search engine listings', re.I))
        self.__reg_exp_list.append(re.compile('Search engines', re.I))
        self.__reg_exp_list.append(re.compile('Subscribe', re.I))
        self.__reg_exp_list.append(re.compile('The following form', re.I))
        self.__reg_exp_list.append(re.compile("This isn't junk", re.I))
        self.__reg_exp_list.append(re.compile("This isn't spam", re.I))
        self.__reg_exp_list.append(re.compile('Undisclosed recipient', re.I))
        self.__reg_exp_list.append(re.compile('Unsubscribe', re.I))
        self.__reg_exp_list.append(re.compile('Visit our website', re.I))
        self.__reg_exp_list.append(re.compile('We hate spam', re.I))
        self.__reg_exp_list.append(re.compile('Web traffic', re.I))
        self.__reg_exp_list.append(re.compile('Will not believe your eyes', re.I))
        self.__reg_exp_list.append(re.compile('Cures baldness', re.I))
        self.__reg_exp_list.append(re.compile('Diagnostics', re.I))
        self.__reg_exp_list.append(re.compile('Fast Viagra delivery', re.I))
        self.__reg_exp_list.append(re.compile('Human growth hormone', re.I))
        self.__reg_exp_list.append(re.compile('Life Insurance', re.I))
        self.__reg_exp_list.append(re.compile('Lose weight', re.I))
        self.__reg_exp_list.append(re.compile('Lose weight spam', re.I))
        self.__reg_exp_list.append(re.compile('Medicine', re.I))
        self.__reg_exp_list.append(re.compile('No medical exams', re.I))
        self.__reg_exp_list.append(re.compile('Online pharmacy', re.I))
        self.__reg_exp_list.append(re.compile('Removes wrinkles', re.I))
        self.__reg_exp_list.append(re.compile('Reverses aging', re.I))
        self.__reg_exp_list.append(re.compile('Stop snoring', re.I))
        self.__reg_exp_list.append(re.compile('Valium', re.I))
        self.__reg_exp_list.append(re.compile('Viagra', re.I))
        self.__reg_exp_list.append(re.compile('Vicodin', re.I))
        self.__reg_exp_list.append(re.compile('Weight loss', re.I))
        self.__reg_exp_list.append(re.compile('Xanax', re.I))
        self.__reg_exp_list.append(re.compile('#1', re.I))
        self.__reg_exp_list.append(re.compile('100% free', re.I))
        self.__reg_exp_list.append(re.compile('100% Satisfied', re.I))
        self.__reg_exp_list.append(re.compile('4U', re.I))
        self.__reg_exp_list.append(re.compile('50%% off', re.I))
        self.__reg_exp_list.append(re.compile('Billion', re.I))
        self.__reg_exp_list.append(re.compile('Billion dollars', re.I))
        self.__reg_exp_list.append(re.compile('Join millions', re.I))
        self.__reg_exp_list.append(re.compile('Join millions of Americans', re.I))
        self.__reg_exp_list.append(re.compile('Million', re.I))
        self.__reg_exp_list.append(re.compile('One hundred percent guaranteed', re.I))
        self.__reg_exp_list.append(re.compile('Thousands', re.I))
        self.__reg_exp_list.append(re.compile('As seen on', re.I))
        self.__reg_exp_list.append(re.compile('Buying judgments', re.I))
        self.__reg_exp_list.append(re.compile('Order status', re.I))
        self.__reg_exp_list.append(re.compile('Buy', re.I))
        self.__reg_exp_list.append(re.compile('Clearance', re.I))
        self.__reg_exp_list.append(re.compile('Orders shipped by', re.I))
        self.__reg_exp_list.append(re.compile('Buy direct', re.I))
        self.__reg_exp_list.append(re.compile('Order', re.I))
        self.__reg_exp_list.append(re.compile('shopper', re.I))
        self.__reg_exp_list.append(re.compile('Dig up dirt on friends', re.I))
        self.__reg_exp_list.append(re.compile('Meet singles', re.I))
        self.__reg_exp_list.append(re.compile('Score with babes', re.I))
        self.__reg_exp_list.append(re.compile('Additional Income', re.I))
        self.__reg_exp_list.append(re.compile('Double your', re.I))
        self.__reg_exp_list.append(re.compile('Earn per week', re.I))
        self.__reg_exp_list.append(re.compile('Home based', re.I))
        self.__reg_exp_list.append(re.compile('Income from home', re.I))
        self.__reg_exp_list.append(re.compile('Money making', re.I))
        self.__reg_exp_list.append(re.compile('Opportunity', re.I))
        self.__reg_exp_list.append(re.compile('While you sleep', re.I))
        self.__reg_exp_list.append(re.compile('Be your own boss', re.I))
        self.__reg_exp_list.append(re.compile('Earn $', re.I))
        self.__reg_exp_list.append(re.compile('Expect to earn', re.I))
        self.__reg_exp_list.append(re.compile('Home employment', re.I))
        self.__reg_exp_list.append(re.compile('Make $', re.I))
        self.__reg_exp_list.append(re.compile('Online biz opportunity', re.I))
        self.__reg_exp_list.append(re.compile('Potential earnings', re.I))
        self.__reg_exp_list.append(re.compile('Work at home', re.I))
        self.__reg_exp_list.append(re.compile('Compete for your business', re.I))
        self.__reg_exp_list.append(re.compile('Earn extra cash', re.I))
        self.__reg_exp_list.append(re.compile('Extra income', re.I))
        self.__reg_exp_list.append(re.compile('Homebased business', re.I))
        self.__reg_exp_list.append(re.compile('Make money', re.I))
        self.__reg_exp_list.append(re.compile('Online degree', re.I))
        self.__reg_exp_list.append(re.compile('University diplomas', re.I))
        self.__reg_exp_list.append(re.compile('Work from home', re.I))
        self.__reg_exp_list.append(re.compile('$$$', re.I))
        self.__reg_exp_list.append(re.compile('Beneficiary', re.I))
        self.__reg_exp_list.append(re.compile('Cash', re.I))
        self.__reg_exp_list.append(re.compile('Cents on the dollar', re.I))
        self.__reg_exp_list.append(re.compile('Claims', re.I))
        self.__reg_exp_list.append(re.compile('Cost', re.I))
        self.__reg_exp_list.append(re.compile('Discount', re.I))
        self.__reg_exp_list.append(re.compile('F r e e', re.I))
        self.__reg_exp_list.append(re.compile('Hidden assets', re.I))
        self.__reg_exp_list.append(re.compile('Incredible deal', re.I))
        self.__reg_exp_list.append(re.compile('Loans', re.I))
        self.__reg_exp_list.append(re.compile('Money', re.I))
        self.__reg_exp_list.append(re.compile('Mortgage rates', re.I))
        self.__reg_exp_list.append(re.compile('One hundred percent free', re.I))
        self.__reg_exp_list.append(re.compile('Price', re.I))
        self.__reg_exp_list.append(re.compile('Quote', re.I))
        self.__reg_exp_list.append(re.compile('Save big money', re.I))
        self.__reg_exp_list.append(re.compile('Subject to credit', re.I))
        self.__reg_exp_list.append(re.compile('Unsecured debt', re.I))
        self.__reg_exp_list.append(re.compile('Affordable', re.I))
        self.__reg_exp_list.append(re.compile('Best price', re.I))
        self.__reg_exp_list.append(re.compile('Cash bonus', re.I))
        self.__reg_exp_list.append(re.compile('Cheap', re.I))
        self.__reg_exp_list.append(re.compile('Collect', re.I))
        self.__reg_exp_list.append(re.compile('Credit', re.I))
        self.__reg_exp_list.append(re.compile('Earn', re.I))
        self.__reg_exp_list.append(re.compile('Fast cash', re.I))
        self.__reg_exp_list.append(re.compile('hidden charges', re.I))
        self.__reg_exp_list.append(re.compile('Insurance', re.I))
        self.__reg_exp_list.append(re.compile('Lowest price', re.I))
        self.__reg_exp_list.append(re.compile('Money back', re.I))
        self.__reg_exp_list.append(re.compile('No cost', re.I))
        self.__reg_exp_list.append(re.compile('Only $', re.I))
        self.__reg_exp_list.append(re.compile('Profits', re.I))
        self.__reg_exp_list.append(re.compile('Refinance', re.I))
        self.__reg_exp_list.append(re.compile('Save up to', re.I))
        self.__reg_exp_list.append(re.compile('They keep your money - no refund!', re.I))
        self.__reg_exp_list.append(re.compile('US dollars', re.I))
        self.__reg_exp_list.append(re.compile('Bargain', re.I))
        self.__reg_exp_list.append(re.compile('Big bucks', re.I))
        self.__reg_exp_list.append(re.compile('Cashcashcash', re.I))
        self.__reg_exp_list.append(re.compile('Check', re.I))
        self.__reg_exp_list.append(re.compile('Compare rates', re.I))
        self.__reg_exp_list.append(re.compile('Credit bureaus', re.I))
        self.__reg_exp_list.append(re.compile('Easy terms', re.I))
        self.__reg_exp_list.append(re.compile('For just $\d\d\d', re.I))
        self.__reg_exp_list.append(re.compile('Income', re.I))
        self.__reg_exp_list.append(re.compile('Investment', re.I))
        self.__reg_exp_list.append(re.compile('Million dollars', re.I))
        self.__reg_exp_list.append(re.compile('Mortgage', re.I))
        self.__reg_exp_list.append(re.compile('No fees', re.I))
        self.__reg_exp_list.append(re.compile('Pennies a day', re.I))
        self.__reg_exp_list.append(re.compile('Pure profit', re.I))
        self.__reg_exp_list.append(re.compile('Save $', re.I))
        self.__reg_exp_list.append(re.compile('Serious cash', re.I))
        self.__reg_exp_list.append(re.compile('Unsecured credit', re.I))
        self.__reg_exp_list.append(re.compile('Why pay more', re.I))
        self.__reg_exp_list.append(re.compile('Accept Credit Cards', re.I))
        self.__reg_exp_list.append(re.compile('Credit card offers', re.I))
        self.__reg_exp_list.append(re.compile('Investment decision', re.I))
        self.__reg_exp_list.append(re.compile('No investment', re.I))
        self.__reg_exp_list.append(re.compile('Stock alert', re.I))
        self.__reg_exp_list.append(re.compile('Cards accepted', re.I))
        self.__reg_exp_list.append(re.compile('Explode your business', re.I))
        self.__reg_exp_list.append(re.compile('No credit check', re.I))
        self.__reg_exp_list.append(re.compile('Requires initial investment', re.I))
        self.__reg_exp_list.append(re.compile('Stock disclaimer statement ', re.I))
        self.__reg_exp_list.append(re.compile('Check or money order', re.I))
        self.__reg_exp_list.append(re.compile('Full refund', re.I))
        self.__reg_exp_list.append(re.compile('No hidden Costs', re.I))
        self.__reg_exp_list.append(re.compile('Sent in compliance', re.I))
        self.__reg_exp_list.append(re.compile('Stock pick', re.I))

    def get_word_counts(self):
        return self.__word_counts


if __name__ == "__main__":
    pass
